# Generated by Django 3.0.1 on 2021-06-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0017_auto_20210620_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
