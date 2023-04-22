# Generated by Django 4.1.6 on 2023-03-28 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0029_order_delivery_method_order_payment_method_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="created_on",
        ),
        migrations.RemoveField(
            model_name="order",
            name="delivery_method",
        ),
        migrations.RemoveField(
            model_name="order",
            name="payment_method",
        ),
        migrations.RemoveField(
            model_name="order",
            name="status",
        ),
        migrations.RemoveField(
            model_name="order",
            name="total_price",
        ),
        migrations.RemoveField(
            model_name="order",
            name="updated_on",
        ),
        migrations.AddField(
            model_name="order",
            name="cart",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="eshop.cart",
            ),
        ),
    ]