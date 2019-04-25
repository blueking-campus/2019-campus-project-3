# -*- coding: utf-8 -*-
from common.mymako import render_mako_context


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt【装饰器引入from account.decorators import login_exempt】
def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/index.html')


def organization_management(request):
    """
    组织管理
    """
    return render_mako_context(request, '/system_management/organization_management.html')
