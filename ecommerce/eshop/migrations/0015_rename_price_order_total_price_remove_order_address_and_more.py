# Generated by Django 4.1.6 on 2023-03-14 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("eshop", "0014_product_product_short_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="price",
            new_name="total_price",
        ),
        migrations.RemoveField(
            model_name="order",
            name="address",
        ),
        migrations.RemoveField(
            model_name="order",
            name="phone",
        ),
        migrations.RemoveField(
            model_name="order",
            name="product",
        ),
        migrations.AlterField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="productvariant",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_variants",
                to="eshop.product",
            ),
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="eshop.order",
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
