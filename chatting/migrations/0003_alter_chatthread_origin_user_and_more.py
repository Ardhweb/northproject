# Generated by Django 5.1.5 on 2025-01-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0002_rename_alpha_user_chatthread_origin_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatthread',
            name='origin_user',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='chatthread',
            name='other_user',
            field=models.IntegerField(),
        ),
    ]
