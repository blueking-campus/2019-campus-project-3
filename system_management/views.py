# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from common.mymako import render_mako_context, render_json
from common.context_processors import mysetting

import json
from bkoauth.utils import transform_uin
from system_management.models import Organization, Award
from system_management.utils import is_reviewer
from system_management.decorators import require_admin


@require_GET
def user_info(request):
    """获取用户信息"""
    uin = request.COOKIES.get('uin', '')
    user_qq = transform_uin(uin)
    user = request.user
    permission = ['apply']
    if user.is_admin():
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


# ===============================================================================
# 组织相关
# ===============================================================================
@require_admin
@require_GET
def organization_management(request):
    """
    组织管理
    """
    organizations = Organization.objects.all()

    org_list = {'org_list': Organization.to_array(organizations)}
    return render_mako_context(request, '/system_management/organization_management.html', org_list)


@csrf_exempt
def add_organization(request):
    """新增组织"""
    result = json.loads(request.body)
    # TODO：valid
    Organization.objects.create_organization(result, request.user)
    return render_json({'result': True, 'data': "add success"})


@require_POST
def get_organization(request):
    """查看组织"""
    result = json.loads(request.body)
    organization_id = int(result['id'])
    try:
        organization = Organization.objects.get(id=organization_id)
    except ObjectDoesNotExist:
        raise Http404("organization does not exist")
    return render_json({'result': True, 'data': organization.to_json()})


@require_POST
def update_organization(request):
    """更新组织"""
    result = json.loads(request.body)
    organization_id = int(result['id'])
    try:
        organization = Organization.objects.filter(id=organization_id)[0]
    except ObjectDoesNotExist:
        raise Http404("organization does not exist")
    Organization.objects.update_organization(organization, result, request.user)
    return render_json({'result': True, 'data': "update success"})


@require_POST
def delete_organization(request):
    """删除组织"""
    result = json.loads(request.body)
    organization_id = int(result['id'])
    try:
        organization = Organization.objects.filter(id=organization_id)
    except ObjectDoesNotExist:
        raise Http404("organization does not exist")
    organization.delete()
    return render_mako_context(request, '/system_management/organization_management.html')


# ===============================================================================
# 奖项相关
# ===============================================================================
@require_admin
def award_management(request):
    """奖项管理"""
    award = Award.objects.all()
    award_list = {'award_list': award}
    return render_mako_context(request, '/system_management/award_management.html', award_list)


@require_POST
@csrf_exempt
def add_award(request):
    result = json.loads(request.body)
    Award.objects.create(name=result['name'],
                         requirement=result['requirement'],
                         level=result['level'],
                         organization=Organization.objects.get(name=result['organization']),
                         begin_time=result['begin_time'],
                         end_time=result['end_time'],
                         appendix_status=result['appendix_status'],
                         status=result['status'], )
    return render_json({'result': True, 'data': "add success"})


@require_POST
def delete_award(request):
    result = json.loads(request.body)
    award_id = int(result['id'])
    try:
        award = Award.objects.filter(id=award_id)
    except ObjectDoesNotExist:
        raise Http404('ObjectDoesNotExist')
    award.delete()
    return render_mako_context(request, '/system_management/award_management.html')


@require_GET
def get_award(request, award_id):
    try:
        award = Award.objects.get(id=award_id)
    except ObjectDoesNotExist:
        raise Http404("Award does not exist")

    return render_mako_context(request, '/system_management/award_info.html', award.to_json())


@require_POST
def update_award(request):
    result = json.loads(request.body)
    award_id = int(result['id'])
    try:
        award = Award.objects.filter(id=award_id)
    except Exception:
        raise Http404("award does not exist")

    award.update(name=result['name'])

    return render_mako_context(request, '/system_management/award_management.html')
