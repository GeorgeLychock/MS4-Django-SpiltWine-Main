# Generated by Django 3.2 on 2022-02-03 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_wine_has_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='body',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.body'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.style'),
        ),
    ]
