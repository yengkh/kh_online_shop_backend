from django.shortcuts import render, redirect
from .models import ImageModel
from django.http import JsonResponse

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        promotion_banner_data = ImageModel()
        promotion_banner_data.title = request.POST.get('title')
        if len(request.FILES) != 0:
            promotion_banner_data.image = request.FILES['image']
        promotion_banner_data.save()
        return redirect('promotion_banner:view_page')
    else:
        promotion_banner_data = ImageModel()
    return render(request, 'promotion_banner/home_page.html')

def view_page(respone):
    promotion_banner_datas = ImageModel.objects.all()
    context  = {
        "promotion_banner_datas" : promotion_banner_datas
    }
    return render(respone, 'promotion_banner/view_page.html', context)

def update_page(respone, id):
    if respone.method == "POST":
        title = respone.POST['title']
        if len(respone.FILES) != 0:
            image = respone.FILES['image']
        update = ImageModel.objects.get(id=id)
        update.title = title
        update.image = image
        update.save()
        return redirect('promotion_banner:view_page')
    promotion_banner_datas = ImageModel.objects.get(id=id)
    return render(respone, 'promotion_banner/update_page.html', {"promotion_banner_datas" : promotion_banner_datas})

def delete_data(request, id):
    promotion_banner_datas = ImageModel.objects.get(id=id)
    promotion_banner_datas.delete()
    return redirect('promotion_banner:view_page')

def get_promotion_banner(request):
    images = ImageModel.objects.all()
    data = [
        {
            "id": str(image.id),
            "title": image.title,
            "image_url": request.build_absolute_uri(image.image.url)
        } for image in images
    ]
    return JsonResponse(data, safe=False)
