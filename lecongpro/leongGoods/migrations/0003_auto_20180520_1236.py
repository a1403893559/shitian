# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leongGoods', '0002_auto_20180520_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='gouwu',
            name='upic',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 20, 12, 36, 1, 61878)),
        ),
    ]
