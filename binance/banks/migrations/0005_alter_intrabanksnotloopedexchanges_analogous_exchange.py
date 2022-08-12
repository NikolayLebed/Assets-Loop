# Generated by Django 3.2.14 on 2022-08-11 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0004_intrabanksnotloopedexchanges_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intrabanksnotloopedexchanges',
            name='analogous_exchange',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='not_looped', to='banks.banksexchangerates'),
        ),
    ]
