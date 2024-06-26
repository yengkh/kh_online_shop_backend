from django.db import models
import uuid

# Create your models here.
class TopBrand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length= 50)
    banner = models.ImageField(upload_to='top_brand_banner')
    upload_time = models.DateTimeField()
    
    def __str__(self) :
        return self.name