# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0004_auto_20190428_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='create_time',
            new_name='pub_time',
        ),
        migrations.RemoveField(
            model_name='award',
            name='create_time',
        ),
        migrations.AddField(
            model_name='award',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u7533\u62a5\u65f6\u95f4', null=True),
        ),
    ]
