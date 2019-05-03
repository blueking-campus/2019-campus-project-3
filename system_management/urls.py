# -*- coding: utf-8 -*-
from django.conf.urls import patterns

urlpatterns = patterns(
    'system_management.views',
    # 首页--your index
    (r'^organization_management/', 'organization_management'),
    (r'^add_organization/', 'add_organization'),
    (r'^update_organization/', 'update_organization'),
    (r'^delete_organization/', 'delete_organization'),
    (r'^get_organization/', 'get_organization'),
    (r'^award_management/', 'award_management'),
)
