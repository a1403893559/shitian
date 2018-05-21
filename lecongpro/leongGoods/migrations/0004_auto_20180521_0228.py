# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('leongGoods', '0003_auto_20180520_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 21, 2, 28, 55, 972647)),
        ),
        migrations.AlterField(
            model_name='gouwu',
            name='ushu',
            field=models.IntegerField(),
        ),
    ]
