# Generated by Django 2.2.4 on 2019-08-25 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='FirstName', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='LastName', max_length=200),
        ),
    ]