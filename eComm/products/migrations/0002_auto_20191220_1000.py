# Generated by Django 2.2.6 on 2019-12-20 04:30

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=products.models.upload_file_path),
        ),
    ]
