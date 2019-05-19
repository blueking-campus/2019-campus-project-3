# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0015_auto_20190510_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='begin_time',
            field=models.DateTimeField(verbose_name='\u5f00\u59cb\u65e5\u671f'),
        ),
    ]
