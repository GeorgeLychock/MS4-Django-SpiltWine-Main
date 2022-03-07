# Generated by Django 3.2 on 2022-03-06 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20220306_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulinaryBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Culinary Brands',
            },
        ),
        migrations.CreateModel(
            name='WineAccessoryBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Wine Accessory Brands',
            },
        ),
        migrations.CreateModel(
            name='WineAccessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('puid', models.CharField(editable=False, max_length=32)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('img_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('has_sizes', models.BooleanField(blank=True, default=False, null=True)),
                ('size', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.wineaccessorybrand')),
            ],
            options={
                'verbose_name_plural': 'Wine Accessory Products',
            },
        ),
        migrations.CreateModel(
            name='Culinary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('puid', models.CharField(editable=False, max_length=32)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('img_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('has_sizes', models.BooleanField(blank=True, default=False, null=True)),
                ('size', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.culinarybrand')),
            ],
            options={
                'verbose_name_plural': 'Culinary Products',
            },
        ),
    ]