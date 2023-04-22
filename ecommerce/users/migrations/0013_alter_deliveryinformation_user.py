# Generated by Django 4.1.6 on 2023-03-28 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_alter_deliveryinformation_address_line1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deliveryinformation",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="delivery_informations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]