from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import ProductCategory
from datetime import datetime

date_time_now = datetime.now()
dt_string = date_time_now.strftime("%d/%m/%Y %H:%M:%S")

# Create your views here.
def home_page(request):
    if request.method == "POST":
        data = ProductCategory()
        data.name = request.POST.get('name')
        data.upload_date = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
        if len(request.FILES) != 0:
            data.image = request.FILES['image']
        data.save()
        return redirect('product_category:view_page')
    else :
        data = ProductCategory()
    return render(request, 'product_category/home_page.html')

def view_page(respone):
    data = ProductCategory.objects.all()
    return render(respone, 'product_category/view_page.html', {'data' : data})

def update_page(respone, id):
    if respone.method == 'POST':
        new_name = respone.POST['name']
        if len(respone.FILES) !=0 :
            image = respone.FILES['image']
        update = ProductCategory.objects.get(id=id)
        update.name = new_name
        update.upload_date = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
        update.image = image
        update.save()
        return redirect('product_category:view_page')
        
    old_data = ProductCategory.objects.get(id=id)
    return render(respone, 'product_category/update_page.html', {'old_data' : old_data})

def delete_function(request, id):
    data = ProductCategory.objects.get(id = id)
    data.delete()
    return redirect('product_category:view_page')

def import_function(request):
    all_datas = ProductCategory.objects.all()
    data = [
        {
            'id' : str(all_data.id),
            'name' : all_data.name,
            'imageUrl' : request.build_absolute_uri(all_data.image.url)
        } for all_data in all_datas
    ]
    return JsonResponse(data, safe=False) 