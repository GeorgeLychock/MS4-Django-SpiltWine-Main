# Generated by Django 3.2 on 2022-02-13 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20220213_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_full_name',
        ),
    ]
