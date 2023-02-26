# Generated by Django 4.1.6 on 2023-02-24 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.product')),
            ],
            options={
                'verbose_name': 'Varianta produktu',
                'verbose_name_plural': 'Varianty produktu',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='eshop/uploads/products')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop.product')),
            ],
            options={
                'verbose_name': 'Produktový obrázek',
                'verbose_name_plural': 'Produktové obrázky',
            },
        ),
    ]
