# Generated by Django 4.1.6 on 2023-04-09 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_category",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blog_post_categories",
                to="blog.postcategory",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.IntegerField(
                choices=[
                    (0, "Draft"),
                    (1, "Publish"),
                    (2, "Promoted"),
                    (3, "Moderator"),
                ],
                default=0,
            ),
        ),
    ]