# Generated by Django 3.2.14 on 2022-08-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0003_intrabanksnotloopedexchanges_analogous_exchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='intrabanksnotloopedexchanges',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
