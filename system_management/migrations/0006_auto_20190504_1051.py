# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0005_auto_20190429_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=20, verbose_name='\u5956\u9879\u7ea7\u522b')),
            ],
            options={
                'verbose_name': '\u5956\u9879\u7ea7\u522b\u9009\u9879',
                'verbose_name_plural': '\u5956\u9879\u7ea7\u522b\u9009\u9879',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('open_id', models.CharField(unique=True, max_length=255, verbose_name='open_id')),
                ('qq', models.CharField(default=b'', unique=True, max_length=20, verbose_name='qq')),
            ],
            options={
                'verbose_name': '\u7528\u6237QQ\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237QQ\u4fe1\u606f',
            },
        ),
        migrations.DeleteModel(
            name='Openid2qq',
        ),
        migrations.AddField(
            model_name='award',
            name='appendix_status',
            field=models.BooleanField(default=False, verbose_name='\u9644\u4ef6\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='award',
            name='level',
            field=models.ForeignKey(to='system_management.LevelChoice'),
        ),
    ]
