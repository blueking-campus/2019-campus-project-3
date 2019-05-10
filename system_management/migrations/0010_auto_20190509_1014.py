# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0009_auto_20190507_1806'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='reviewer',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='staff',
        ),
        migrations.AlterField(
            model_name='organization',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 10, 14, 32, 293000),
                                       verbose_name='\u7533\u62a5\u65f6\u95f4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organization',
            name='update_person',
            field=models.ForeignKey(verbose_name='\u66f4\u65b0\u4eba', to=settings.AUTH_USER_MODEL),
        ),
    ]
