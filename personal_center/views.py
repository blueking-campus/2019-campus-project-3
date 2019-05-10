# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from common.mymako import render_mako_context, render_json

import json
from bkoauth.utils import transform_uin
from .models import Apply
from system_management.models import Award, OrganizationUser


# Create your models here.
# ===============================================================================
# 申请相关
# ===============================================================================
def my_apply(request):
    """
    我的申报
    """
    applyed_list = Apply.objects.filter(user=request.user)  # 我的已申报记录
    award_applyed = Apply.objects.filter(user=request.user).values_list('award')  # 已申报的奖项

    uin = request.COOKIES.get('uin', '')
    user_qq = transform_uin(uin)  # 得到用户QQ
    organ = OrganizationUser.objects.get(user=user_qq).organization  # 得到用户组织
    award_can_apply_list = Award.objects.filter(organization=organ, status=True)  # 得到有权限且生效中的奖项
    apply_list = []  # 可申报奖项
    for award in award_can_apply_list:
        if (award.id,) not in award_applyed:
            apply_list.append(award)
    data = {'apply_list': apply_list, 'applyed_list': applyed_list}
    return render_mako_context(request, '/personal_center/my_apply.html', data)


def applying(request, award_id):
    try:
        award = Award.objects.get(id=award_id)
    except ObjectDoesNotExist:
        raise Http404("Award does not exist")
    return render_mako_context(request, '/personal_center/apply.html', award.to_json())


def get_apply_info(request, apply_id):
    return render_mako_context(request, '/personal_center/apply.html')


def add_apply(request):
    data = json.loads(request.body)

    Apply.objects.create(award_id=data['id'], user=request.user, **data)

    return render_json({'result': True, 'data': "add success"})


def my_review(request):
    """
    我的审核
    """

    return render_mako_context(request, '/personal_center/my_review.html')
