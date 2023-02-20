# Generated by Django 4.1.6 on 2023-02-18 17:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Uživatel',
                'verbose_name_plural': 'Uživatelé',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(blank=True, max_length=500)),
                ('address_line2', models.CharField(blank=True, max_length=500)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Zákazník',
                'verbose_name_plural': 'Zákazníci',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('posted_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Kontaktní formulář',
                'verbose_name_plural': 'Kontaktní formuláře',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_sku', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.TextField()),
                ('product_image', models.ImageField(upload_to='eshop/uploads/products')),
                ('product_inventory', models.IntegerField(default=0)),
                ('product_price', models.FloatField(default=0)),
                ('original_price', models.FloatField(default=0)),
                ('product_evaluation', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkty',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('category_description', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Kategorie produktu',
                'verbose_name_plural': 'Kategorie produktů',
            },
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_name', models.CharField(max_length=50)),
                ('inventory_description', models.TextField()),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Sklad produktu',
                'verbose_name_plural': 'Sklad produktů',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_title', models.CharField(max_length=30, verbose_name='Příznaky')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Příznak',
                'verbose_name_plural': 'Příznaky',
            },
        ),
        migrations.CreateModel(
            name='ProductPriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(default='CZK', max_length=3)),
                ('price_list_name', models.CharField(max_length=50)),
                ('price_list_description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eshop.product')),
            ],
            options={
                'verbose_name': 'Ceník produktu',
                'verbose_name_plural': 'Ceníky produktů',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eshop.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_tag',
            field=models.ManyToManyField(blank=True, to='eshop.tag'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('phone', models.CharField(blank=True, default='', max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Pending'), (1, 'Placed'), (2, 'Payed')], default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.product')),
            ],
            options={
                'verbose_name': 'Objednávka',
                'verbose_name_plural': 'Objednávky',
            },
        ),
    ]
