# Generated by Django 3.2 on 2022-02-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0003_rename_cellar_wine_name_cellaritem_cellar_wine_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellaritem',
            name='quantity_onhand',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
