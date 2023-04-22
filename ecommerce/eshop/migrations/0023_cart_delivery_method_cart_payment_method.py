# Generated by Django 4.1.6 on 2023-03-25 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0022_alter_cartdiscount_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="delivery_method",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carts",
                to="eshop.deliverymethod",
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="payment_method",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carts",
                to="eshop.paymentmethod",
            ),
        ),
    ]
