# Generated by Django 3.1.13 on 2021-07-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210716_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('', 'Role'), ('MODERATOR', 'Moderator'), ('QUESTIONER', 'Questioner'), ('HELPER', 'Helper')], default='QUESTIONER', max_length=255, null=True, verbose_name='User Role'),
        ),
    ]