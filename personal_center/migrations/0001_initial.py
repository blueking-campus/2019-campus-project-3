# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0004_auto_20190428_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('applicant', models.CharField(max_length=255, verbose_name='\u7533\u8bf7\u4eba/\u56e2\u961f')),
                ('introduction', models.TextField(verbose_name='\u4e8b\u8ff9\u4ecb\u7ecd')),
                ('status', models.IntegerField(verbose_name='\u5956\u9879\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u7533\u62a5\u65f6\u95f4')),
                ('award', models.ForeignKey(to='system_management.Award')),
            ],
            options={
                'verbose_name': '\u5956\u9879\u7533\u8bf7',
                'verbose_name_plural': '\u5956\u9879\u7533\u8bf7',
            },
        ),
    ]
