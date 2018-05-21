# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('leongGoods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gouwu',
            name='udanjia',
            field=models.DecimalField(default=2, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 20, 12, 26, 28, 102476)),
        ),
    ]
