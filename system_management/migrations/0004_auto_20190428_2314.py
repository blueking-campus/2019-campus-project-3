# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0003_auto_20190428_0025'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Awards',
            new_name='Award',
        ),
    ]
