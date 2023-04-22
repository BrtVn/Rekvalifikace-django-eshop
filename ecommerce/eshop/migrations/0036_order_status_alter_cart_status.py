# Generated by Django 4.1.6 on 2023-04-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0035_order_total_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("DRAFT", "Draft"),
                    ("PLACED", "Placed"),
                    ("PENDING", "Pending"),
                    ("PAID", "Paid"),
                ],
                default=0,
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="cart",
            name="status",
            field=models.CharField(
                choices=[("DRAFT", "Draft"), ("SAVED", "Saved"), ("PLACED", "Placed")],
                default=0,
                max_length=20,
            ),
        ),
    ]