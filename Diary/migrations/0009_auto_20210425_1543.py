# Generated by Django 3.0.1 on 2021-04-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0008_auto_20210425_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diarygroup',
            options={'ordering': ['rank']},
        ),
        migrations.AddField(
            model_name='diarygroup',
            name='rank',
            field=models.IntegerField(default=1),
        ),
    ]
