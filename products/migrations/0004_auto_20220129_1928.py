# Generated by Django 3.2 on 2022-01-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_body_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='varietal',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='varietal',
            name='img_file_name',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='varietal',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
