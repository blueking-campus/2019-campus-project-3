# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_center', '0002_auto_20190429_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='status',
            field=models.IntegerField(verbose_name='\u5956\u9879\u72b6\u6001', choices=[(0, '\u7533\u62a5\u4e2d'), (1, '\u672a\u901a\u8fc7'), (2, '\u5df2\u901a\u8fc7'), (3, '\u672a\u83b7\u5956'), (4, '\u5df2\u83b7\u5956')]),
        ),
    ]
