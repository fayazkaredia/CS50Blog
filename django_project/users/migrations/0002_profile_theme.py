# Generated by Django 3.0.8 on 2020-07-11 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='theme',
            field=models.TextField(default='light'),
        ),
    ]
