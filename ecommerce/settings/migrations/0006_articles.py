# Generated by Django 4.1.6 on 2023-04-09 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_post_category"),
        ("settings", "0005_alter_generalinfo_company_info"),
    ]

    operations = [
        migrations.CreateModel(
            name="Articles",
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
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.post"
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
            },
        ),
    ]
