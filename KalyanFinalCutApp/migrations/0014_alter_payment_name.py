# Generated by Django 3.2.9 on 2023-03-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KalyanFinalCutApp', '0013_auto_20230330_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Name',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]