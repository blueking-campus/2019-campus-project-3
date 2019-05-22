# -*- coding: utf-8 -*-
from django.conf.urls import patterns

urlpatterns = patterns(
    'system_management.views',
    (r'^organization_management/$', 'organization_management'),
    (r'^add_organization/$', 'add_organization'),
    (r'^update_organization/$', 'update_organization'),
    (r'^delete_organization/$', 'delete_organization'),
    (r'^get_organization_name/$', 'get_organization_name'),
    (r'^get_organization/$', 'get_organization'),

    (r'^award_management/', 'award_management'),
    (r'^add_award/', 'add_award'),
    (r'^delete_award/', 'delete_award'),
    (r'^award/([0-9]{1,})/$', 'award_info'),
    (r'^get_award/([0-9]{1,})/$', 'get_award'),
    (r'^update_award/$', 'update_award'),
    (r'^clone/$', 'clone'),
    (r'^clone_preview/$', 'clone_preview'),
)
