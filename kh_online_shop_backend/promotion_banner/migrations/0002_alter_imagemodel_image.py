# Generated by Django 5.0.6 on 2024-06-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion_banner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='promotion_banner_'),
        ),
    ]