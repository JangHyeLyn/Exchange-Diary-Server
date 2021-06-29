# Generated by Django 3.0.1 on 2021-06-20 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_auto_20210605_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='created_at',
            new_name='_created_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='updated_at',
            new_name='_updated_at',
        ),
        migrations.AlterField(
            model_name='user',
            name='_created_at',
            field=models.DateTimeField(auto_now_add=True, db_column='created_at'),
        ),
        migrations.AlterField(
            model_name='user',
            name='_updated_at',
            field=models.DateTimeField(auto_now=True, db_column='updated_at'),
        ),
    ]
