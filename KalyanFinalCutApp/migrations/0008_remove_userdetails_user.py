# Generated by Django 4.1.3 on 2023-01-16 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KalyanFinalCutApp', '0007_userdetails_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
    ]
