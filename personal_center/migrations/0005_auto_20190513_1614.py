# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('personal_center', '0004_auto_20190509_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='status',
            field=models.IntegerField(default=b'0', verbose_name='\u5956\u9879\u72b6\u6001',
                                      choices=[(0, '\u5ba1\u6838\u4e2d'), (1, '\u5df2\u901a\u8fc7'),
                                               (2, '\u672a\u901a\u8fc7'), (3, '\u5df2\u83b7\u5956'),
                                               (4, '\u672a\u83b7\u5956')]),
        ),
    ]
