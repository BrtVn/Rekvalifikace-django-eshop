# Generated by Django 4.1.6 on 2023-04-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0030_remove_order_created_on_remove_order_delivery_method_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="note",
            field=models.CharField(default="", max_length=1000),
            preserve_default=False,
        ),
    ]