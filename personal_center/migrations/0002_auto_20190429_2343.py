# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('personal_center', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='create_time',
            new_name='pub_time',
        ),
    ]
