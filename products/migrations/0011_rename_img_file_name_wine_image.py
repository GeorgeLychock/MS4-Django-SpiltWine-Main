# Generated by Django 3.2 on 2022-02-18 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_wine_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wine',
            old_name='img_file_name',
            new_name='image',
        ),
    ]
