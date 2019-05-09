# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0006_auto_20190504_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='level',
            field=models.CharField(max_length=20, verbose_name='\u5956\u9879\u7b49\u7ea7'),
        ),
    ]
