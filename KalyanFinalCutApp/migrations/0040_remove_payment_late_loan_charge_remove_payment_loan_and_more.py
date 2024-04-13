# Generated by Django 4.2.7 on 2023-11-17 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KalyanFinalCutApp', '0039_loan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='Late_Loan_Charge',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='Loan',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='Loan_Balance',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='Loan_Installment',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='Loan_Interest',
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_intrest_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_intrest_rate',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_principle',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]