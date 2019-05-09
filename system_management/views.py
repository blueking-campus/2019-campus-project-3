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


@require_admin
@require_GET
def organization_management(request):
    """
    组织管理
    """
    organizations = Organization.objects.all()
    org_list = {'org_list': organizations}
    return render_mako_context(request, '/system_management/organization_management.html', org_list)


@csrf_exempt
def add_organization(request):
    result = json.loads(request.body)
    # TODO：valid
    Organization.objects.create_organization(result, request.user)
    return render_json({'result': True, 'data': "add success"})


@require_GET
def get_organization(request):
    organization_id = request.GET.get('id')
    try:
        organization = Organization.objects.get(id=organization_id)
    except ObjectDoesNotExist:
        raise Http404("organization does not exist")
    return render_json(organization.to_json())


@require_POST
def update_organization(request):
    result = json.loads(request.body)
    organization_id = int(result['id'])
    try:
        organization = Organization.objects.filter(id=organization_id)
    except ObjectDoesNotExist:
        raise Http404("organization does not exist")
    Organization.objects.update_organization(organization, result, request.user)
    return render_json({'result': True, 'data': "update success"})


@require_POST
def delete_organization(request):
    result = json.loads(request.body)
    organization_id = int(result['id'])
    try:
        organization = Organization.objects.filter(id=organization_id)
    except ObjectDoesNotExist:
        raise Http404("organization does not exist")
    organization.delete()
    return render_mako_context(request, '/system_management/organization_management.html')


def award_management(request):
    """奖项管理"""
    award = Award.objects.all()
    award_list = {'award_list': award}
    return render_mako_context(request, '/system_management/award_management.html', award_list)


@csrf_exempt
def add_award(request):
    result = json.loads(request.body)
    Award.objects.create(name=result['name'],
                         requirement=result['requirement'],
                         level=result['level'],
                         organization=result['organization'],
                         begin_time=result['begin_time'],
                         end_time=result['end_time'],
                         appendix_status=result['appendix_status'],
                         status=result['status'], )
    return render_json("add success")


def delete_award(request):
    result = json.loads(request.body)
    award_id = int(result['id'])
    try:
        award = Award.objects.filter(id=award_id)
        award.delete()
    except Exception as e:
        raise Http404(e)
    return render_mako_context(request, '/system_management/award_management.html')


@require_GET
def get_award(request):
    try:
        award_id = request.GET.get('id')
        award = Award.objects.get(id=award_id)
        data = {
            'id': award.id,
            'name': award.name,
            'requirement': award.requirement,
            'status': award.status,
            'level': award.level,
            'organization': award.organization,
            'begin_time': award.begin_time,
            'end_time': award.end_time,
        }
    except Exception:
        raise Http404("award does not exist")
    return render_mako_context(request, '/system_management/award_info.html', data)


@require_POST
def update_organization(request):
    try:
        result = json.loads(request.body)
        award_id = int(result['id'])

        award = Award.objects.filter(id=award_id)
        award.update(name=result['name'])
        award.update(reviewer=result['reviewer'])
        award.update(staff=result['staff'])
        award.update(update_person=request.user)
    except Exception:
        raise Http404("award does not exist")
    return render_mako_context(request, '/system_management/award_management.html')
