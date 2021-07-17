# Generated by Django 3.1.13 on 2021-07-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='users.Profile'),
        ),
    ]