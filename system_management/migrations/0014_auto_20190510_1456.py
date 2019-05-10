# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0013_auto_20190510_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='status',
            field=models.BooleanField(verbose_name='\u72b6\u6001',
                                      choices=[('0', '\u751f\u6548\u4e2d'), ('1', '\u5df2\u8fc7\u671f')]),
        ),
    ]
