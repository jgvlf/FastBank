# Generated by Django 4.1 on 2022-11-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_bank_api', '0006_alter_valealimentacao_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planosaude',
            name='pay_installment_date',
            field=models.DateField(blank=True),
        ),
    ]