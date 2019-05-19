# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0009_auto_20190507_1806'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LevelChoice',
        ),
        migrations.AlterField(
            model_name='award',
            name='level',
            field=models.CharField(max_length=20, verbose_name='\u5956\u9879\u7b49\u7ea7',
                                   choices=[('0', '\u4e2d\u5fc3\u7ea7'), ('1', '\u90e8\u95e8\u7ea7'),
                                            ('2', '\u5c0f\u7ec4\u7ea7'), ('3', '\u516c\u53f8\u7ea7')]),
        ),
        migrations.AlterField(
            model_name='award',
            name='organization',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u7ec4\u7ec7', to='system_management.Organization'),
        ),
    ]
