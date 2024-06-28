from django.db import models
import uuid

# Create your models here.
class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length= 50)
    image = models.ImageField(upload_to="product_category_banner")
    upload_date = models.DateTimeField()
    
    def __str__(self):
        return self.name
