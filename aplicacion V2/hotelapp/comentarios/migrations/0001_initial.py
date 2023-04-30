# Generated by Django 4.2 on 2023-04-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idd', models.PositiveSmallIntegerField(default=5, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=200)),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('texto', models.TextField()),
                ('location', models.TextField(max_length=200)),
                ('hotel', models.TextField(max_length=200)),
                ('negativo', models.BooleanField(default=False)),
            ],
        ),
    ]