# -*- coding: utf-8 -*-
from common.mymako import render_mako_context
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
