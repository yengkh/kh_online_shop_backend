# Generated by Django 5.0.6 on 2024-06-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_commentmodel_id_alter_imagemodel_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='black_color',
            field=models.ImageField(blank=True, null=True, upload_to='product_image_black'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='white_color',
            field=models.ImageField(blank=True, null=True, upload_to='product_image_white'),
        ),
    ]
