# Generated by Django 3.2.23 on 2024-08-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'admin'), ('USER', 'user')], default='USER', max_length=10),
        ),
    ]
