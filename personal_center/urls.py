# -*- coding: utf-8 -*-
from django.conf.urls import patterns

urlpatterns = patterns(
    'personal_center.views',
    # 首页--your index
    (r'^my_apply/$', 'my_apply'),
    (r'^applying/([0-9]{1,})/$', 'applying'),
    (r'^add_apply/$', 'add_apply'),
    (r'^apply_info/([0-9]{1,})/$', 'get_apply_info'),

    (r'^my_review', 'my_review'),
)
