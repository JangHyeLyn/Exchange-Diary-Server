# Generated by Django 3.0 on 2021-04-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0004_auto_20210211_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarygroup',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
