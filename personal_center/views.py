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
    applyed_list = Apply.objects.filter(user=request.user).order_by('status')  # 我的已申报记录
    award_applyed = Apply.objects.filter(user=request.user).values_list('award')  # 已申报的奖项

    uin = request.COOKIES.get('uin', '')
    user_qq = transform_uin(uin)  # 得到用户QQ
    organ = OrganizationUser.objects.get(user=user_qq, type=u'1').organization  # 得到用户组织
    award_can_apply_list = Award.objects.filter(organization=organ, status=True)  # 得到有权限且生效中的奖项
    apply_list = []  # 可申报奖项
    for award in award_can_apply_list:
        if (award.id,) not in award_applyed:
            apply_list.append(award)
    data = {'apply_list': apply_list, 'applyed_list': applyed_list}
    return render_mako_context(request, '/personal_center/my_apply.html', data)


def applying(request, award_id):
    """申报奖项"""
    try:
        award = Award.objects.get(id=award_id)
    except ObjectDoesNotExist:
        raise Http404("Award does not exist")
    data = award.to_json()
    apply_obj = Apply.objects.filter(award=award, user=request.user)
    if apply_obj:
        data['apply_obj'] = apply_obj[0]
    return render_mako_context(request, '/personal_center/apply.html', data)


def add_apply(request):
    """提交申报"""
    data = json.loads(request.body)

    Apply.objects.create(award_id=data['id'], user=request.user, **data)

    return render_json({'result': True, 'data': "add success"})


def get_apply_info(request, apply_id):
    """查看我的申请"""
    try:
        apply_obj = Apply.objects.get(id=apply_id)
    except ObjectDoesNotExist:
        raise Http404("Apply does not exist")
    data = apply_obj.award.to_json()
    data['apply_obj'] = apply_obj
    data['type'] = 'get_apply_info'
    return render_mako_context(request, '/personal_center/apply_info.html', data)


def update_apply(request):
    """编辑申报"""
    data = json.loads(request.body)
    try:
        apply_obj = Apply.objects.get(id=data['id'])
    except ObjectDoesNotExist:
        raise Http404("Apply does not exist")
    apply_obj.applicant = data['applicant']
    apply_obj.introduction = data['introduction']
    apply_obj.save()
    return render_json({'result': True, 'data': "update success"})


# ===============================================================================
# 审核相关
# ===============================================================================
def my_review(request):
    """
    我的审核
    """
    uin = request.COOKIES.get('uin', '')
    user_qq = transform_uin(uin)  # 得到用户QQ
    try:
        organ = OrganizationUser.objects.get(user=user_qq, type=u'1').organization  # 得到用户组织
    except ObjectDoesNotExist:
        raise Http404("Apply does not exist")
    apply_list = Apply.objects.filter(award__organization=organ).order_by('status')
    data = {'apply_list': apply_list}
    return render_mako_context(request, '/personal_center/my_review.html', data)


def review_apply(request):
    """审核申请"""
    data = json.loads(request.body)
    apply_obj = Apply.objects.get(id=data['id'])
    status = 1 if data['status'] else 2
    apply_obj.review(data['status'])
    return render_json({'result': True, 'data': "review success"})


def remark_apply(request, apply_id):
    """评奖"""
    try:
        apply_obj = Apply.objects.get(id=apply_id)
    except ObjectDoesNotExist:
        raise Http404("Apply does not exist")
    data = apply_obj.award.to_json()
    data['apply_obj'] = apply_obj
    return render_mako_context(request, '/personal_center/review.html', data)


def commit_remark(request):
    """提交评奖结果"""
    data = json.loads(request.body)
    apply_obj = Apply.objects.get(id=data['id'])
    status = 3 if data['status'] else 4
    apply_obj.review(status, data['remark'])

    return render_json({'result': True, 'data': "remark success"})


def get_review_info(request, apply_id):
    """查看我的申请"""
    try:
        apply_obj = Apply.objects.get(id=apply_id)
    except ObjectDoesNotExist:
        raise Http404("Apply does not exist")
    data = apply_obj.award.to_json()
    data['apply_obj'] = apply_obj
    data['type'] = 'get_review_info'
    return render_mako_context(request, '/personal_center/apply_info.html', data)
