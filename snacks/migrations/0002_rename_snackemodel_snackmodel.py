# Generated by Django 3.2.9 on 2021-12-06 20:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SnackeModel',
            new_name='SnackModel',
        ),
    ]
