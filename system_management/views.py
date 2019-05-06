# -*- coding: utf-8 -*-
from common.mymako import render_mako_context


# Create your views here.
def organization_management(request):
    """
    组织管理
    """
    return render_mako_context(request, '/system_management/organization_management.html')
