# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal_center', '0003_auto_20190507_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='remark',
            field=models.TextField(verbose_name='\u8bc4\u8bed', blank=True),
        ),
        migrations.AddField(
            model_name='apply',
            name='user',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apply',
            name='award',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe5\xa5\x96\xe9\xa1\xb9',
                                    to='system_management.Award'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='status',
            field=models.IntegerField(default=b'0', verbose_name='\u5956\u9879\u72b6\u6001',
                                      choices=[(0, '\u7533\u62a5\u4e2d'), (1, '\u672a\u901a\u8fc7'),
                                               (2, '\u5df2\u901a\u8fc7'), (3, '\u672a\u83b7\u5956'),
                                               (4, '\u5df2\u83b7\u5956')]),
        ),
    ]
