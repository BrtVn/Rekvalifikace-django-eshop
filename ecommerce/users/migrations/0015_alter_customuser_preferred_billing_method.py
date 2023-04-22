# Generated by Django 4.1.6 on 2023-04-01 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0014_customuser_preferred_billing_method_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="preferred_billing_method",
            field=models.OneToOneField(
                blank=True,
                limit_choices_to={"user": models.F("pk")},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="preferred_by_user",
                to="users.billinginformation",
                verbose_name="Preferred billing method",
            ),
        ),
    ]
