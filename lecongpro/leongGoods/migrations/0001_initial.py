# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gtitle', models.CharField(max_length=40)),
                ('gpic', models.ImageField(upload_to='/static/media/')),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('isdelete', models.BooleanField(default=False)),
                ('gclick', models.IntegerField(default=0)),
                ('gunit', models.IntegerField(default=500)),
                ('gjianjie', models.TextField()),
                ('gpub_date', models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 15, 3, 18, 42, 480199))),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('t_title', models.CharField(max_length=20)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='leongGoods.TypeInfo'),
        ),
    ]
