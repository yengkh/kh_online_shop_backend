from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('promotion-banner/', include('promotion_banner.urls')),
    path('top-brands/', include('top_brands.urls')),
    path('product-category/', include('product_category.urls')),
    path('products/', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)