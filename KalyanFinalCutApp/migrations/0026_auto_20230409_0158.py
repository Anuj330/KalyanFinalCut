# Generated by Django 3.2.9 on 2023-04-08 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KalyanFinalCutApp', '0025_auto_20230409_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order_id',
        ),
        migrations.AddField(
            model_name='payment',
            name='S_no',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]