# Generated by Django 3.0 on 2021-02-09 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
    ]
