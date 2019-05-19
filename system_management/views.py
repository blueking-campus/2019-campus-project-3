# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from common.mymako import render_mako_context, render_json

import json
from system_management.models import Organization, Award
from system_management.decorators import require_admin


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
    award = Award.objects.all().order_by('-pub_time')
    award_list = {'award_list': award}
    return render_mako_context(request, '/system_management/award_management.html', award_list)


@require_POST
def add_award(request):
    result = json.loads(request.body)
    Award.objects.create(name=result['name'],
                         requirement=result['requirement'],
                         level=result['level'],
                         organization=Organization.objects.get(id=result['organization']),
                         begin_time=result['begin_time'],
                         end_time=result['end_time'],
                         appendix_status=result['appendix_status'],
                         status=result['status'], )
    return render_json({'result': True, 'data': "add success"})


@require_GET
def get_organization_name(request):
    """添加奖项组织时查询组织"""
    organizations = Organization.objects.all()
    data = Organization.to_name(organizations)
    return render_json({"results": data})


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
def award_info(request, award_id):
    """查看奖项详情页面"""
    try:
        award = Award.objects.get(id=award_id)
    except ObjectDoesNotExist:
        raise Http404("Award does not exist")
    data = award.to_json()
    data['apply_all'] = award.apply_all
    return render_mako_context(request, '/system_management/award_info.html', data)


@require_GET
def get_award(request, award_id):
    """得到奖项信息"""
    try:
        award = Award.objects.get(id=award_id)
    except ObjectDoesNotExist:
        raise Http404("Award does not exist")

    return render_json(award.to_json())


@require_POST
def update_award(request):
    """更新奖项
    返回组织id
    """
    result = json.loads(request.body)
    award_id = int(result['id'])
    try:
        award = Award.objects.get(id=award_id)
    except Exception:
        raise Http404("award does not exist")

    award.name = result['name']
    award.requirement = result['requirement']
    award.level = result['level']
    award.organization = Organization.objects.get(id=result['organization'])
    award.begin_time = result['begin_time']
    award.end_time = result['end_time']
    award.status = result['status']
    award.save()
    return render_json({'result': True, 'data': "update success"})
