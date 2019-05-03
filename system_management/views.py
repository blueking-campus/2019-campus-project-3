# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect,csrf_exempt

from common.mymako import render_mako_context
from system_management.models import Organization, Award


# Create your views here.
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
    print result
    Organization.objects.create(name=result['name'],
                                reviewer=result['reviewer'],
                                staff=result['staff'],
                                update_person=request.user)
    return render_mako_context(request, '/system_management/organization_management.html')


def update_organization(request):
    result = json.loads(request.body)
    organization_id = int(result['id'])

    organization = Organization.objects.filter(id=organization_id)
    organization.update(name=result['name'])
    organization.update(reviewer=result['reviewer'])
    organization.update(staff=result['staff'])
    organization.update(update_person=request.user)

    return render_mako_context(request, '/system_management/organization_management.html')


def delete_organization(request):
    result = json.loads(request.body)
    organization_id = int(result['id'])
    organization = Organization.objects.filter(id=organization_id)
    organization.delete()
    return render_mako_context(request, '/system_management/organization_management.html')


def get_organization(request):
    try:
        organization_id = request.GET.get('id')
        organization = Organization.objects.get(id=organization_id)
        data = {
            'id': organization.id,
            'name': organization.name,
            'reviewer': organization.reviewer,
            'staff': organization.staff,
            'update_person': organization.update_person,
        }
    except Exception as e:
        print e.message
    return render_mako_context(request, '/system_management/organization_management.html', data)


def award_management(request):
    award = Award.objects.all()
    award_list = {'award_list': award}
    return render_mako_context(request, '/system_management/award_management.html', award_list)

def delete_award(request):
    result = json.loads(request.body)
    award_id = int(result['id'])
    award = Award.objects.filter(id=award_id)
    award.delete()
    return render_mako_context(request, '/system_management/award_management.html')
