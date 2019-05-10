# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0012_auto_20190510_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='apply_num',
        ),
        migrations.RemoveField(
            model_name='award',
            name='awarded_num',
        ),
    ]
