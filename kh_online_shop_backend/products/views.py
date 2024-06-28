from django.shortcuts import render
from datetime import datetime
from .models import Products, CommentModel, ImageModel, PriceModel, RatingStarModel

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
        product = Products.objects.create(
            name = name, 
            detail = product_detail, 
            product_brand = product_brand, 
            product_type = product_type,
            upload_date = upload_date,
            )
        product.save()
        
        if len(request.FILES) != 0:
            # 2 Product Image
            black_image = request.FILES['blakcolor']
            white_image = request.FILES['whitecolor']
            other_image_one = request.FILES['othercolorone']
            other_image_two = request.FILES['othercolortwo']
            image_title = f"{name} images"
            image = ImageModel.objects.create(
                products = product, 
                black_color = black_image, 
                white_color = white_image,
                other_color_one = other_image_one,
                other_color_two = other_image_two,
                title = image_title,
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
            products = product,
        )
        product_price.save()
        
        # 4 Product Rating Stars
        get_stars = RatingStarModel.objects.last()

        if get_stars:
            if get_stars.total_stars != 0.0 and get_stars.user_rate != 0:
                total_star = get_stars.total_stars
                total_user = get_stars.user_rate
                average_star = get_stars.average_star
            else:
                total_star = 0.0
                total_user = 0
                average_star = 0.0
        else:
            total_star = 0.0
            total_user = 0
            average_star = 0.0

        product_star = request.POST.get('rating-star')
        star_title = f"{name} stars"

        if float(product_star) != 0.0:
            product_star = float(product_star)
            total_stars = total_star +  product_star
            total_users = total_user + 1
            average_stars = float(total_stars / total_users)
        else:
            total_stars = total_star
            total_users = total_user
            average_stars = average_star

        user_rating_star = RatingStarModel.objects.create(
            title=star_title,
            user_rate=total_users,
            total_stars=total_stars,
            average_star= float('{:.1f}'.format(average_stars)),
            products=product,
        )
        user_rating_star.save()

        
        # 5 Product Comments
        comment_title = f'{name} comment'
        user_name = 'John'
        comment_total = 12
        comment_content = "Hello World"
        product_comment = CommentModel.objects.create(
            title = comment_title,
            user_name = user_name,
            comment_total = comment_total,
            content = comment_content,
            products = product,
        )
        product_comment.save()
            
    return render(request, 'products/home_page.html')
