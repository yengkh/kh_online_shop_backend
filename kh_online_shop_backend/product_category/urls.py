from django.urls import path
from . import views

app_name = "product_category"

urlpatterns = [
     path('', views.home_page, name="home_page"),
     path('view-page/', views.view_page, name="view_page"),
     path('update-page/<uuid:id>/', views.update_page, name="update_page"),
     path('delete_function/<uuid:id>/', views.delete_function, name="delete_function"),
     path('import_function/', views.import_function, name="import_function"),
]
