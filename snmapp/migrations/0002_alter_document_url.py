# Generated by Django 5.0.6 on 2024-05-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
