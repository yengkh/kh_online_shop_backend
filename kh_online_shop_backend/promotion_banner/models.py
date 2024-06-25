from django.db import models
import uuid

class ImageModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='promotion_banner')

    def __str__(self):
        return self.title
