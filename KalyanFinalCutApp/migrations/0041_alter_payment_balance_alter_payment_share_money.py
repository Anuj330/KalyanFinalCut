# Generated by Django 4.2.7 on 2023-11-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KalyanFinalCutApp', '0040_remove_payment_late_loan_charge_remove_payment_loan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Balance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Share_Money',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
