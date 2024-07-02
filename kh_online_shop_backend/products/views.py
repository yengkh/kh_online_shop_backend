from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from .models import Products, ImageModel, PriceModel, RatingStarModel

date_time_now = datetime.now()
dt_string = date_time_now.strftime("%d/%m/%Y %H:%M:%S")

# Create your views here.
def home_page(request):
    if request.method == "POST":
        # 1 Product
        name = request.POST.get('name')
        product_detail = request.POST.get('product_detail')
        upload_date = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
        product_type = request.POST.get('product_type')
        product_brand = request.POST.get('product_brand')
        product_quantity = request.POST.get('product_quantity')
        product = Products.objects.create(
            name = name, 
            detail = product_detail, 
            product_brand = product_brand, 
            product_type = product_type,
            upload_date = upload_date,
            product_quantity = product_quantity
            )
        product.save()
        
        # 2 Product Image
        if len(request.FILES) != 0:
            black_image = request.FILES.get('blakcolor')
            white_image = request.FILES.get('whitecolor')
            other_image_one = request.FILES.get('othercolorone')
            other_image_two = request.FILES.get('othercolortwo')
            
            image_title = f"{name} images"
            
            # Create ImageModel only if at least one image file is provided
            if any([black_image, white_image, other_image_one, other_image_two]):
                image = ImageModel.objects.create(
                    product=product,
                    black_color=black_image if black_image else None,
                    white_color=white_image if white_image else None,
                    other_color_one=other_image_one if other_image_one else None,
                    other_color_two=other_image_two if other_image_two else None,
                    title=image_title,
                )
                image.save()
        
        # 3 Product Price
        price = request.POST.get('price')
        discount_rating = request.POST.get('dicount-rate')
        price_title = f"{name} price"
        discount_price = (float(price) * float(discount_rating))/100
        total_price = float(price) - float(discount_price)
        product_price = PriceModel.objects.create(
            title = price_title,
            default_price = price,
            discount_rate = discount_rating,
            discount_price = discount_price,
            total_price = float('{:.2f}'.format(total_price)),
            product = product,
        )
        product_price.save()
        
        # 4 Product Rating Stars
        rating = request.POST.get('rating-star')
        title = f"{name} Rating"
        average_stars = float(rating) 
        user_rate = 1
        rating_star = RatingStarModel.objects.create(
            title = title,
            total_stars = rating,
            user_rate = user_rate,
            average_star = average_stars,
            product = product,
        )
        rating_star.save()
         
    return render(request, 'products/home_page.html')

def view_page(respone):
    data = Products.objects.all().prefetch_related('pricemodel_set', 'commentmodel_set', 'ratingstarmodel_set', 'imagemodel_set')
    return render(respone, 'products/view_page.html', {'data' : data})

def update_page(request, id):
    if request.method == "POST":
        name = request.POST['name']
        detail = request.POST['product_detail']
        type = request.POST['product_type']
        brand = request.POST['product_brand']
        qty = request.POST['product_quantity']
        
        black_image = request.FILES.get('blakcolor')
        white_image = request.FILES.get('whitecolor')
        other_image_one = request.FILES.get('othercolorone')
        other_image_two = request.FILES.get('othercolortwo')
        
        price = request.POST['price']
        discount_rate = request.POST['dicount_rate']
        discount_price = (float(price) * float(discount_rate))/100
        total_price = float(price) - float(discount_price)
        
        total_stars = request.POST['rating-star']
        user_rate = request.POST['user_rate']
        
        product = get_object_or_404(Products.objects.prefetch_related('pricemodel_set', 'commentmodel_set', 'ratingstarmodel_set', 'imagemodel_set'), id=id)
        
        product.name = name
        product.detail = detail
        product.product_type = type
        product.product_brand = brand
        product.product_quantity = qty
        product.save()

        # Update ImageModel
        images = product.imagemodel_set.first()  # Assuming only one related image set exists
        if images:
            if black_image:
                images.black_color = black_image
            if white_image:
                images.white_color = white_image
            if other_image_one:
                images.other_color_one = other_image_one
            if other_image_two:
                images.other_color_two = other_image_two
            images.save()

        # Update PriceModel
        prices = product.pricemodel_set.first()  # Assuming only one related price set exists
        if prices:
            prices.default_price = price
            prices.discount_rate = discount_rate
            prices.discount_price = "{:.2f}".format(float(discount_price))
            prices.total_price = total_price
            prices.save()

        # Update RatingStarModel
        ratings = product.ratingstarmodel_set.first()  # Assuming only one related rating set exists
        try:
            average_star = "{:.2f}".format(float(total_stars) / float(user_rate) if user_rate != 0 else 0)
            ratings.total_stars = total_stars
            ratings.user_rate = user_rate
            ratings.average_star = average_star
            ratings.save()
        except ZeroDivisionError:
            ratings.average_star = 0.0
        finally:
            ratings.save()
                
        return redirect('products:view_page')
        
    # Use prefetch_related on the queryset
    queryset = Products.objects.prefetch_related('pricemodel_set', 'commentmodel_set', 'ratingstarmodel_set', 'imagemodel_set')
    old_data = get_object_or_404(queryset, id=id) 
    return render(request, 'products/update_page.html', {'old_data': old_data})

def delete_page(request, id):
    product = get_object_or_404(Products, id=id)
    product.delete()
    return redirect('products:view_page')

def export_function_2(request):
    products = Products.objects.all().prefetch_related('pricemodel_set', 'commentmodel_set', 'ratingstarmodel_set', 'imagemodel_set')
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'detail': product.detail,
            'upload_date': product.upload_date.strftime('%Y-%m-%d %H:%M:%S'),
            'product_type': product.product_type,
            'product_brand': product.product_brand,
            'product_quantity' : product.product_quantity,
            'comments': [
                {
                    'title': comment.title,
                    'user_name': comment.user_name,
                    'comment_total': comment.comment_total,
                    'content': comment.content,
                } for comment in product.commentmodel_set.all()
            ],
            'prices': [
                {
                    'title': price.title,
                    'default_price': price.default_price,
                    'discount_rate': price.discount_rate,
                    'discount_price': price.discount_price,
                    'total_price': price.total_price,
                } for price in product.pricemodel_set.all()
            ],
            'ratings': [
                {
                    'title': rating.title,
                    'total_stars': rating.total_stars,
                    'user_rate': rating.user_rate,
                    'average_star': rating.average_star,
                } for rating in product.ratingstarmodel_set.all()
            ],
            'images': [
                {
                    'black_color': request.build_absolute_uri(image.black_color.url) if image.black_color else None,
                    'white_color': request.build_absolute_uri(image.white_color.url) if image.white_color else None,
                    'other_color_one': request.build_absolute_uri(image.other_color_one.url) if image.other_color_one else None,
                    'other_color_two': request.build_absolute_uri(image.other_color_two.url) if image.other_color_two else None,
                } for image in product.imagemodel_set.all()
            ],
        } for product in products
    ]
    return JsonResponse(data, safe=False)
