# Generated by Django 3.0.1 on 2021-05-08 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Diary', '0011_diary_promise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='now_writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='now_writers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diaries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diarygroup',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_diary_group_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diarygroupmember',
            name='diary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group', to='Diary.Diary'),
        ),
        migrations.AlterField(
            model_name='diarygroupmember',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='Diary.DiaryGroup'),
        ),
        migrations.AlterField(
            model_name='diarymember',
            name='diary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='Diary.Diary'),
        ),
        migrations.AlterField(
            model_name='diarymember',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='joins', to=settings.AUTH_USER_MODEL),
        ),
    ]
