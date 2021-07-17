# Generated by Django 3.1.13 on 2021-07-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_auto_20210717_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True, verbose_name='Topic Slug'),
        ),
    ]
