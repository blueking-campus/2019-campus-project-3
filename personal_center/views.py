# -*- coding: utf-8 -*-
from common.mymako import render_mako_context

from bkoauth.utils import transform_uin
from .models import Apply
from system_management.models import Award

# Create your views here.
def my_apply(request):
    """
    我的申报
    """
    uin = request.COOKIES.get('uin', '')
    user_qq = transform_uin(uin)
    user = request.user
    applyed_list = Apply.objects.all()
    apply_list = applyed_list
    return render_mako_context(request, '/personal_center/my_apply.html', {'apply_list': apply_list})


def my_review(request):
    """
    我的审核
    """

    return render_mako_context(request, '/personal_center/my_review.html')
