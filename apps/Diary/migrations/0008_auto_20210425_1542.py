# Generated by Django 3.0.1 on 2021-04-25 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0007_auto_20210425_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diarygroup',
            options={'ordering': ['-pk']},
        ),
        migrations.RemoveField(
            model_name='diarygroup',
            name='rank',
        ),
    ]
