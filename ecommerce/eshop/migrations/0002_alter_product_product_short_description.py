# Generated by Django 4.1.6 on 2023-04-25 14:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_short_description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
