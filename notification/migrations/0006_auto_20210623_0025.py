# Generated by Django 3.0.1 on 2021-06-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_auto_20210605_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(choices=[('invite', '새로운 일기장에 초대 받았어요!')], max_length=100),
        ),
    ]
