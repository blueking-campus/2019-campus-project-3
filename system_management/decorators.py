# coding=utf-8
from functools import wraps

from django.http import HttpResponse
from django.utils.decorators import available_attrs

from bkoauth.utils import transform_uin
from system_management.utils import is_reviewer


def require_admin(func):
    """
    验证是否管理员装饰器
    """

    @wraps(func, assigned=available_attrs(func))
    def inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponse(status=401, content=u'需要管理员权限')
        return func(request, *args, **kwargs)

    return inner


def require_reviewer(func):
    """
    验证是否负责人
    """

    @wraps(func, assigned=available_attrs(func))
    def inner(request, *args, **kwargs):
        uin = request.COOKIES.get('uin', '')
        user_qq = transform_uin(uin)
        if not is_reviewer(request.user, user_qq):
            return HttpResponse(status=401, content=u'需要负责人权限')
        return func(request, *args, **kwargs)

    return inner
