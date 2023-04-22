# Generated by Django 4.1.6 on 2023-02-28 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_deliveryinformation_alias"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="profile_image",
            field=models.ImageField(blank=True, upload_to="users/uploads/users"),
        ),
        migrations.AlterField(
            model_name="deliveryinformation",
            name="alias",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="deliveryinformation",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="delivery_informations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
