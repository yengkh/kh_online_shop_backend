# Generated by Django 5.0.6 on 2024-06-28 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_imagemodel_black_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='products',
        ),
        migrations.RemoveField(
            model_name='imagemodel',
            name='products',
        ),
        migrations.RemoveField(
            model_name='pricemodel',
            name='products',
        ),
        migrations.RemoveField(
            model_name='ratingstarmodel',
            name='products',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.products'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.products'),
        ),
        migrations.AddField(
            model_name='pricemodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='products.products'),
        ),
        migrations.AddField(
            model_name='products',
            name='comment_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_comments', to='products.commentmodel'),
        ),
        migrations.AddField(
            model_name='products',
            name='image_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.imagemodel'),
        ),
        migrations.AddField(
            model_name='products',
            name='price_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_prices', to='products.pricemodel'),
        ),
        migrations.AddField(
            model_name='products',
            name='rating_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_ratings', to='products.ratingstarmodel'),
        ),
        migrations.AddField(
            model_name='ratingstarmodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='products.products'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='content',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='user_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pricemodel',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ratingstarmodel',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
