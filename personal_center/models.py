# -*- coding: utf-8 -*-
from django.db import models

from system_management.models import Award
from account.models import BkUser


# Create your models here.
# ===============================================================================
# 申请相关的表
# ===============================================================================
class Apply(models.Model):
    applicant = models.CharField(u"申请人/团队", max_length=255)
    introduction = models.TextField(u"事迹介绍")
    # todo: 附件
    STATUS_CHOICES = (
        (0, u'申报中'),
        (1, u'未通过'),
        (2, u'已通过'),
        (3, u'未获奖'),
        (4, u'已获奖'),
    )
    status = models.IntegerField(u"奖项状态", choices=STATUS_CHOICES, default='0')
    award = models.ForeignKey(to=Award, verbose_name="申请奖项", on_delete=models.CASCADE)
    remark = models.TextField(u"评语", blank=True)
    user = models.ForeignKey(BkUser)
    pub_time = models.DateTimeField(u"申报时间", auto_now_add=True)

    class Meta:
        verbose_name = u"奖项申请"
        verbose_name_plural = verbose_name

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.applicant
