# Generated by Django 3.2.14 on 2022-07-18 13:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateP2PBinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Update date')),
                ('duration', models.DurationField(default=datetime.timedelta(0))),
            ],
        ),
        migrations.CreateModel(
            name='P2PBinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(choices=[('USDT', 'USDT'), ('BUSD', 'BUSD'), ('BTC', 'BTC')], max_length=4)),
                ('trade_type', models.CharField(choices=[('BUY', 'buy'), ('SELL', 'sell')], max_length=4)),
                ('fiat', models.CharField(choices=[('RUB', 'rub'), ('USD', 'usd'), ('EUR', 'eur')], max_length=3)),
                ('pay_type', models.CharField(choices=[('Tinkoff', 'Tinkoff'), ('Wise', 'Wise'), ('RosBank', 'RosBank'), ('RUBfiatbalance', 'RUBfiatbalance')], max_length=15)),
                ('price', models.FloatField(blank=True, default=None, null=True)),
                ('update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datas', to='parses_p2p.updatep2pbinance')),
            ],
        ),
    ]
