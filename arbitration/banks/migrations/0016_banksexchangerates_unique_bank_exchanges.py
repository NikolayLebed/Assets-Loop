# Generated by Django 3.2.14 on 2022-11-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0015_alter_banksexchangeratesupdates_bank'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='banksexchangerates',
            constraint=models.UniqueConstraint(fields=('bank', 'from_fiat', 'to_fiat', 'currency_market'), name='unique_bank_exchanges'),
        ),
    ]
