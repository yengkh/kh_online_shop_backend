# Generated by Django 5.0.6 on 2024-06-27 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_brands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topbrand',
            name='upload_time',
            field=models.DateTimeField(),
        ),
    ]