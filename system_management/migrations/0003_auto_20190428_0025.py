# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0002_auto_20190427_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u7533\u62a5\u5956\u9879')),
                ('requirement', models.TextField(verbose_name='\u8bc4\u5956\u6761\u4ef6')),
                ('level', models.CharField(max_length=20, verbose_name='\u5956\u9879\u7ea7\u522b')),
                ('organization', models.CharField(max_length=255, verbose_name='\u6240\u5c5e\u7ec4\u7ec7')),
                ('begin_time', models.DateTimeField(auto_now=True, verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('end_time', models.DateTimeField(verbose_name='\u7ed3\u675f\u65e5\u671f')),
                ('status', models.BooleanField(verbose_name='\u72b6\u6001')),
                ('apply_num', models.IntegerField(verbose_name='\u7533\u62a5\u4eba\u6570')),
                ('awarded_num', models.IntegerField(verbose_name='\u83b7\u5956\u4eba\u6570')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
        migrations.AlterField(
            model_name='organization',
            name='reviewer',
            field=models.CharField(max_length=255, verbose_name='\u8d1f\u8d23\u4eba\u5458'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='staff',
            field=models.TextField(verbose_name='\u53c2\u8bc4\u4eba\u5458'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='update_person',
            field=models.CharField(max_length=30, verbose_name='\u66f4\u65b0\u4eba'),
        ),
    ]
