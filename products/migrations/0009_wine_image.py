# Generated by Django 3.2 on 2022-02-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220203_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
