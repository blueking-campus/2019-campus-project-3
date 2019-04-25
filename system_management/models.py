# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
# ===============================================================================
# 组织相关的表
# ===============================================================================
class Organization(models.Model):
    """"""
    # LEVEL = (
    #     #     ('DE', 'Department'),
    #     #     ('CE', 'Center'),
    #     #     ('CO', 'Company'),
    #     # )
    name = models.CharField(u"组织名称", max_length=255, unique=True)
    # level = models.CharField(max_length=2, verbose_name="部门级别", choices=LEVEL)
    leader = models.CharField(u"负责人员", max_length=255)
    member = models.TextField(u"参评人员")
    create_person = models.CharField(u"更新人", max_length=30)
    create_time = models.DateTimeField(u"申报时间", auto_now_add=True)
