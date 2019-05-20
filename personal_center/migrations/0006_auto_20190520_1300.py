# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_center', '0005_auto_20190513_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appendix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u6587\u4ef6\u540d\u79f0')),
                ('path', models.FilePathField(verbose_name='\u6587\u4ef6\u5730\u5740')),
            ],
        ),
        migrations.AddField(
            model_name='apply',
            name='appendix',
            field=models.ForeignKey(verbose_name='\u9644\u4ef6', blank=True, to='personal_center.Appendix', null=True),
        ),
    ]
