# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zzh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uname',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uname', models.CharField(max_length=15)),
                ('upwd', models.CharField(max_length=25)),
            ],
        ),
    ]
