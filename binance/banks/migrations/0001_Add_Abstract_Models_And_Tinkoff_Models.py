# Generated by Django 3.2.14 on 2022-07-29 16:48

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TinkoffUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Update date')),
                ('duration', models.DurationField(default=datetime.timedelta(0))),
            ],
            options={
                'db_table': 'TinkoffUpdates',
            },
        ),
    ]
