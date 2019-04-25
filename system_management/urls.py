# -*- coding: utf-8 -*-
from django.conf.urls import patterns

urlpatterns = patterns(
    'system_management.views',
    # 首页--your index
    (r'^organization_management', 'organization_management'),
)
