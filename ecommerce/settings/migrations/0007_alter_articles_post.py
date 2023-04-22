# Generated by Django 4.1.6 on 2023-04-09 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_post_category"),
        ("settings", "0006_articles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articles",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="settings_posts",
                to="blog.post",
            ),
        ),
    ]
