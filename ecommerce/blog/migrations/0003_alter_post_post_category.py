# Generated by Django 4.1.6 on 2023-04-08 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_postcategory_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_category",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blog_post_categories",
                to="blog.postcategory",
            ),
        ),
    ]
