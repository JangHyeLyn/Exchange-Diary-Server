# Generated by Django 3.0.1 on 2021-05-16 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0013_auto_20210516_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diaries', to='Diary.DiaryGroup'),
        ),
    ]