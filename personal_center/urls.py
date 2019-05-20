# -*- coding: utf-8 -*-
from django.conf.urls import patterns

urlpatterns = patterns(
    'personal_center.views',
    # 首页--your index
    (r'^my_apply/$', 'my_apply'),
    (r'^applying/([0-9]{1,})/$', 'applying'),
    (r'^add_apply/$', 'add_apply'),
    (r'^update_apply/$', 'update_apply'),
    (r'^get_apply_info/([0-9]{1,})/$', 'get_apply_info'),
    (r'^renew/([0-9]{1,})/$', 'renew'),

    (r'^upload_appendix/$', 'upload_appendix'),
    (r'^remove_appendix/$', 'remove_appendix'),
    (r'^download_appendix/$', 'download_appendix'),

    (r'^my_review/$', 'my_review'),
    (r'^review_apply/$', 'review_apply'),
    (r'^remark_apply/([0-9]{1,})/$', 'remark_apply'),
    (r'^commit_remark/$', 'commit_remark'),
    (r'^get_review_info/([0-9]{1,})$', 'get_review_info'),


)
