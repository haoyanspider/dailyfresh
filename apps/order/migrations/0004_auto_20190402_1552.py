# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-02 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20190325_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='trade_no',
            field=models.CharField(default=1, max_length=128, verbose_name='支付编号'),
        ),
    ]
