# Generated by Django 4.1.6 on 2023-03-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0010_alter_product_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="productcategory",
            name="slug",
            field=models.SlugField(default="", max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
