# Generated by Django 3.2.9 on 2023-03-30 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KalyanFinalCutApp', '0011_auto_20230327_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='Membership_number',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='phone_number',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]