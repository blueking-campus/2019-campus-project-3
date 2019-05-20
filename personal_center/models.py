# -*- coding: utf-8 -*-
from django.db import models

from system_management.models import Award
from account.models import BkUser
from qcloud_cos import CosS3Client
from config.settings_custom import config


# Create your models here.
# ===============================================================================
# 申请相关的表
# ===============================================================================
class Appendix(models.Model):
    """附件表"""
    name = models.CharField(u'文件名称', max_length=255)
    path = models.FilePathField(u'文件地址')

    def get_url(self):
        client = CosS3Client(config)
        response = client.get_presigned_download_url(
            Bucket='awarding-1257208110',
            Key=self.path
        )
        return response

    class Meta:
        verbose_name = u"附件"
        verbose_name_plural = verbose_name

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.path
    # def to_json(self):
    #     return {
    #         'name': self.name,
    #         'url': self.getFileUrl(self.path),
    #         'id': self.id
    #     }


class Apply(models.Model):
    applicant = models.CharField(u"申请人/团队", max_length=255)
    introduction = models.TextField(u"事迹介绍")
    appendix = models.ForeignKey(Appendix, verbose_name=u'附件', null=True, blank=True)
    STATUS_CHOICES = (
        (0, u'审核中'),
        (1, u'已通过'),
        (2, u'未通过'),
        (3, u'已获奖'),
        (4, u'未获奖'),
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

    def review(self, status, remark=''):
        self.status = status
        self.remark = remark
        self.save()


