# Generated by Django 4.1 on 2022-11-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_bank_api', '0008_alter_planosaude_pay_installment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planosaude',
            name='pay_installment_date',
            field=models.DateField(null=True),
        ),
    ]
