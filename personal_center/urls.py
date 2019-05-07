# -*- coding: utf-8 -*-
from django.conf.urls import patterns

urlpatterns = patterns(
    'personal_center.views',
    # 首页--your index
    (r'^my_apply', 'my_apply'),
    (r'^my_review', 'my_review'),
)
