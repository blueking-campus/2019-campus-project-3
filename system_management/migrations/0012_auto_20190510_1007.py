# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0011_auto_20190509_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='level',
            field=models.CharField(max_length=1, verbose_name='\u5956\u9879\u7b49\u7ea7',
                                   choices=[('0', '\u5c0f\u7ec4\u7ea7'), ('1', '\u90e8\u95e8\u7ea7'),
                                            ('2', '\u4e2d\u5fc3\u7ea7'), ('3', '\u516c\u53f8\u7ea7')]),
        ),
    ]
