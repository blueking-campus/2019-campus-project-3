# -*- coding: utf-8 -*-
from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    # 首页--your index
    (r'^$', 'home'),
    # (r'^organization_management/$', 'organization_management'),
)
