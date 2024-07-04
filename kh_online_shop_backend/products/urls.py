from django.urls import path
from . import views
app_name = "products"

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('export-function/', views.export_function_2, name='export_function_2'),
    path('view-page/', views.view_page, name="view_page"),
    path('update-page/<uuid:id>/', views.update_page, name='update_page'),
    path('delete-page/<uuid:id>/', views.delete_page, name='delete_page'),
    path('search-by-type/<str:p_type>/', views.search_by_type, name='search_by_type'),
    path('search-by-brand/<str:p_brand>/', views.search_product_by_brand, name="search_product_by_brand"),
]
