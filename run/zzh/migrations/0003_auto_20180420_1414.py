# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zzh', '0002_uname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uname1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('yonghu', models.CharField(max_length=15)),
                ('mima', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('qmima', models.CharField(max_length=25)),
                ('wenti', models.CharField(max_length=25)),
                ('daan', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Uname',
        ),
    ]
