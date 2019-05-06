# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name',
                 models.CharField(max_length=255, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
        ),
    ]
