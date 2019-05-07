# -*- coding: utf-8 -*-
from common.mymako import render_mako_context
from .models import Apply


# Create your views here.
def my_apply(request):
    """
    我的申报
    """
    apply_list = Apply.objects.all()
    # Apply.objects.values_list('applicant', 'introduction')

    return render_mako_context(request, '/personal_center/my_apply.html', {'apply_list': apply_list})


def my_review(request):
    """
    我的审核
    """

    return render_mako_context(request, '/personal_center/my_review.html')
