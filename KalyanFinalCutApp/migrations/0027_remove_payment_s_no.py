# Generated by Django 3.2.9 on 2023-04-08 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KalyanFinalCutApp', '0026_auto_20230409_0158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='S_no',
        ),
    ]
