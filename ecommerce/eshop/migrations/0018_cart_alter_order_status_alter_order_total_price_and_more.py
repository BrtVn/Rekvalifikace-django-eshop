# Generated by Django 4.1.6 on 2023-03-14 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("eshop", "0017_remove_order_product_alter_order_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=12),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Draft"), (1, "Placed"), (2, "Pending"), (3, "Payed")],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=12),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="eshop.cart",
                    ),
                ),
                (
                    "product_variant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="eshop.productvariant",
                    ),
                ),
            ],
        ),
    ]