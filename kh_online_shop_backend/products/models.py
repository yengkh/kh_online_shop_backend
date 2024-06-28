from django.db import models
import uuid

# Create your models here.
class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    detail = models.TextField(max_length= 1500)
    upload_date = models.DateTimeField()
    product_type = models.CharField(max_length=20)
    product_brand = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class ImageModel(models.Model):
    title = models.CharField()
    black_color = models.ImageField(upload_to="product_image_black")
    white_color = models.ImageField(upload_to="product_image_white")
    other_color_one = models.ImageField(upload_to="product_image_other_one")
    other_color_two = models.ImageField(upload_to="product_image_other_two")
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class PriceModel(models.Model):
    title = models.CharField()
    default_price = models.FloatField()
    discount_rate = models.FloatField()
    discount_price = models.FloatField()
    total_price = models.FloatField()
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class RatingStarModel(models.Model):
    title = models.CharField()
    total_stars = models.FloatField()
    user_rate = models.IntegerField()
    average_star = models.FloatField()
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title

class CommentModel(models.Model):
    title = models.CharField()
    user_name = models.CharField()
    comment_total = models.IntegerField()
    content = models.CharField()
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
