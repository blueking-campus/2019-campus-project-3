# -*- coding: utf-8 -*-
from django.views.decorators.http import require_GET

from common.mymako import render_mako_context, render_json
from common.context_processors import mysetting

from bkoauth.utils import transform_uin
from system_management.utils import is_reviewer
from personal_center.models import Apply
from system_management.models import Award
# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt【装饰器引入from account.decorators import login_exempt】


def home(request):
    """
    首页
    """
    award_list = Award.objects.filter(status=True)
    apply_list = Apply.objects.filter(status=3)
    data = {'award_list': award_list, 'apply_list': apply_list}
    return render_mako_context(request, '/home_application/index.html', data)


@require_GET
def user_info(request):
    """获取用户信息"""
    uin = request.COOKIES.get('uin', '')
    user_qq = transform_uin(uin)
    user = request.user
    permission = ['apply']
    if user.is_superuser:
        permission.append('admin')
    if is_reviewer(user, user_qq):
        permission.append('reviewer')

    setting = mysetting(request)
    data = {
        'nick': setting['NICK'],
        'avatar': setting['AVATAR'],
        'permission': permission
    }
    return render_json(data)