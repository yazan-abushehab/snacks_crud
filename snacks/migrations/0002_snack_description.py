# Generated by Django 4.2.2 on 2023-06-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='description',
            field=models.TextField(default='Feel free'),
        ),
    ]
