# Generated by Django 4.2 on 2023-04-27 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='single',
            name='negativo',
            field=models.BooleanField(default=False),
        ),
    ]
