# Generated by Django 4.1.6 on 2023-04-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_post_post_category_alter_post_status"),
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
                    (3, "Moderator"),
                ],
                default=0,
            ),
        ),
    ]
