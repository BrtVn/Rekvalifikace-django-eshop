# Generated by Django 4.1.6 on 2023-03-10 16:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0011_productcategory_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productvariant",
            old_name="size",
            new_name="variant",
        ),
    ]
