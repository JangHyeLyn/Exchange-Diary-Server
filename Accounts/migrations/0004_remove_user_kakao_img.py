# Generated by Django 3.0 on 2021-04-11 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20210210_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='kakao_img',
        ),
    ]
