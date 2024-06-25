from django.urls import path
from . import views

app_name = 'promotion_banner' 

urlpatterns = [
    path('', views.home_page, name= "home_page"),
    path('view-page/', views.view_page, name= "view_page"),
    path('update-page/<uuid:id>/', views.update_page, name= "update_page"),
    path('delete-data/<uuid:id>/', views.delete_data, name="delete_data"),
    path('get-promotion-banner/', views.get_promotion_banner, name="get_promotion_banner"),
]