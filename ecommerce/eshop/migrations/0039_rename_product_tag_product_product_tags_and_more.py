# Generated by Django 4.1.6 on 2023-04-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0038_remove_product_original_price_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="product_tag",
            new_name="product_tags",
        ),
        migrations.RemoveField(
            model_name="tag",
            name="created_at",
        ),
        migrations.AddField(
            model_name="tag",
            name="color",
            field=models.CharField(default="#16621c", max_length=7),
            preserve_default=False,
        ),
    ]
