# Generated by Django 4.1.6 on 2023-04-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_post_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.IntegerField(
                choices=[
                    (0, "Draft"),
                    (1, "Published"),
                    (2, "Promoted"),
                    (3, "Useful links"),
                ],
                default=0,
            ),
        ),
    ]
