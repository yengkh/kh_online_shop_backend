from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import TopBrand
from datetime import datetime

date_time_now = datetime.now()
dt_string = date_time_now.strftime("%d/%m/%Y %H:%M:%S")
# Create your views here.
def add_brands(request):
    if request.method == "POST":
        data = TopBrand()
        data.name = request.POST.get('name')
        data.upload_time = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
        if len(request.FILES) != 0 :
            data.banner = request.FILES['image']
            
        data.save()
        return redirect('top_brands:view_page')
    else :
        data = TopBrand()    
    return render(request, 'top_brands/home_page.html')

def view_page(request):
    data = TopBrand.objects.all()
    context = {
        "data" : data
    }
    return render (request, 'top_brands/view_page.html', context)

def delete_page(request, id):
    data = TopBrand.objects.get(id=id)
    data.delete()
    return redirect('top_brands:view_page')

def update_page(request, id):
    if request.method == "POST":
        name = request.POST['name']
        if len(request.FILES) !=0 :
            image = request.FILES['image']
        update = TopBrand.objects.get(id=id)
        update.name = name
        update.banner = image
        update.upload_time = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
        update.save()
        return redirect('top_brands:view_page')
    
    datas = TopBrand.objects.get(id=id)
    return render (request, 'top_brands/update_page.html', {'datas' : datas})

def get_product_brand(request) :
    images = TopBrand.objects.all()
    data = [
        {
            "id": str(image.id),
            'name' : image.name,
            'imageUrl' : request.build_absolute_uri(image.banner.url)
        } for image in images
    ]
    return JsonResponse(data, safe=False)

