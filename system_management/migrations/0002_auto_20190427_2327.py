# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('system_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Openid2qq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('open_id', models.CharField(unique=True, max_length=255, verbose_name='open_id')),
                ('qq', models.CharField(unique=True, max_length=20, verbose_name='qq')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u7533\u62a5\u65f6\u95f4', null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='reviewer',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u8d1f\u8d23\u4eba\u5458'),
        ),
        migrations.AddField(
            model_name='organization',
            name='staff',
            field=models.TextField(default=b'', verbose_name='\u53c2\u8bc4\u4eba\u5458'),
        ),
        migrations.AddField(
            model_name='organization',
            name='update_person',
            field=models.CharField(default=b'', max_length=30, verbose_name='\u66f4\u65b0\u4eba'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='\u7ec4\u7ec7\u540d\u79f0'),
        ),
    ]
