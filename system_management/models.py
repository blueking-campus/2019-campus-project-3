# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
# ===============================================================================
# 组织相关的表
# ===============================================================================
class Organization(models.Model):
    """组织表"""
    name = models.CharField(u"组织名称", max_length=255, unique=True)
    # level = models.CharField(max_length=2, verbose_name="部门级别", choices=LEVEL)
    reviewer = models.CharField(u"负责人员", max_length=255)
    staff = models.TextField(u"参评人员")
    update_person = models.CharField(u"更新人", max_length=30)
    pub_time = models.DateTimeField(u"申报时间", auto_now_add=True, null=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name


class OrganizationUser(models.Model):
    organization = models.ForeignKey(Organization)
    user = models.CharField(max_length=20, verbose_name='人员qq号')
    TYPE_CHOICES = (
        (u'0', u'负责人员'),
        (u'1', u'参评人员'),
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)


class UserInfo(models.Model):
    """open_id和qq的映射表"""
    open_id = models.CharField(u"open_id", max_length=255, unique=True)
    qq = models.CharField(u"qq", max_length=20, default="", unique=True)

    class Meta:
        verbose_name = u'用户QQ信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return 'id: %d' % self.id


# ===============================================================================
# 奖项相关的表
# ===============================================================================
class LevelChoice(models.Model):
    level = models.CharField( u'奖项级别', max_length=20)

    class Meta:
        verbose_name = u'奖项级别选项'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.level


class Award(models.Model):
    name = models.CharField(u"申报奖项", max_length=255)
    requirement = models.TextField(u"评奖条件")
    level = models.CharField(u"奖项等级", max_length=20)
    organization = models.CharField(u"所属组织", max_length=255)
    begin_time = models.DateTimeField(u"开始日期", auto_now=True)
    end_time = models.DateTimeField(u"结束日期")
    status = models.BooleanField(u"状态")
    appendix_status = models.BooleanField(u"附件状态", default=False)
    # TODO: appendix
    apply_num = models.IntegerField(u"申报人数", )
    awarded_num = models.IntegerField(u"获奖人数")
    pub_time = models.DateTimeField(u"申报时间", auto_now_add=True, null=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name


