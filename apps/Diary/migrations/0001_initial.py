# Generated by Django 3.1.3 on 2020-12-22 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('now_page', models.IntegerField(default=1)),
                ('total_page', models.IntegerField(choices=[(20, 'Low'), (30, 'Normal'), (50, 'High')], default=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('now_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='now_writer', to='Accounts.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='DiaryMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='Diary.diary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mydiary', to='Accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='DiaryContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='Diary.diary')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycontent', to='Accounts.user')),
            ],
        ),
    ]
