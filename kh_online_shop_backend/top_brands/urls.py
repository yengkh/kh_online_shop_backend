from django.urls import path
from . import views

app_name = 'top_brands' 

urlpatterns = [
    path('', views.add_brands, name= "add_brands"),
    path('view-page/', views.view_page, name= "view_page"),
    path('delete-page/<uuid:id>/', views.delete_page, name= "delete_page"),
    path('update-page/<uuid:id>/', views.update_page, name="update-page"),
    path('get-product-brand/', views.get_product_brand, name= "get_product_brand")
]
