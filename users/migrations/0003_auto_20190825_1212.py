# Generated by Django 2.2.4 on 2019-08-25 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190825_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
    ]