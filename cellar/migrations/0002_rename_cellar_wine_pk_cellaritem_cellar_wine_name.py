# Generated by Django 3.2 on 2022-02-05 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cellaritem',
            old_name='cellar_wine_pk',
            new_name='cellar_wine_name',
        ),
    ]
