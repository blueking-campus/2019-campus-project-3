# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_management', '0007_auto_20190504_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=20, verbose_name=b'\xe4\xba\xba\xe5\x91\x98qq\xe5\x8f\xb7')),
                ('type', models.CharField(max_length=1, choices=[('0', '\u8d1f\u8d23\u4eba\u5458'), ('1', '\u53c2\u8bc4\u4eba\u5458')])),
                ('organization', models.ForeignKey(to='system_management.Organization')),
            ],
        ),
    ]
