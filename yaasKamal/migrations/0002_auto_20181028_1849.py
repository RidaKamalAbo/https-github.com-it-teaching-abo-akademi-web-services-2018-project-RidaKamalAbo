# Generated by Django 2.1.2 on 2018-10-28 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaasKamal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 18, 49, 36, 653827)),
        ),
    ]
