# -*- coding: utf-8 -*-

from django.db import models

from account.models import BkUser


# Create your models here.
# ===============================================================================
# 组织相关的表
# ===============================================================================
class OrganizationManager(models.Manager):
    """组织表Manager"""
    def create_organization(self, data, user):
        obj = self.create(name=data['name'], update_person=user)
        OrganizationUser.create_reviewers(list(set(data['reviewers'])), obj)
        OrganizationUser.create_members(list(set(data['members'])), obj)
        return obj

    def update_organization(self, obj, data, user):
        obj.name = data['name']
        obj.update_person = user
        obj.save(update_fields=['name', 'update_person'])
        OrganizationUser.del_members(obj)
        OrganizationUser.del_reviewers(obj)
        OrganizationUser.create_reviewers(list(set(data['reviewers'])), obj)
        OrganizationUser.create_members(list(set(data['members'])), obj)


class Organization(models.Model):
    """组织表"""
    name = models.CharField(u"组织名称", max_length=255, unique=True)

    update_person = models.ForeignKey(BkUser, verbose_name=u"更新人")
    pub_time = models.DateTimeField(u"申报时间", auto_now_add=True)

    objects = OrganizationManager()

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'reviewers': OrganizationUser.get_reviewers(self),
            'members': OrganizationUser.get_members(self),
            'update_person': self.update_person.get_full_name(),
            'pub_time': self.pub_time,
        }


class OrganizationUser(models.Model):
    """组织人员表"""
    organization = models.ForeignKey(Organization)
    user = models.CharField(max_length=20, verbose_name='人员qq号')
    TYPE_CHOICES = (
        (u'0', u'负责人员'),
        (u'1', u'参评人员'),
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    @classmethod
    def create_reviewers(cls, reviewers, organ):
        for item in reviewers:
            obj = cls(user=item, organization=organ, type=u'0')
            obj.save()

    @classmethod
    def create_members(cls, members, organ):
        for item in members:
            obj = cls(user=item, organization=organ, type=u'1')
            obj.save()

    @classmethod
    def del_reviewers(cls, organ):
        cls.objects.filter(organization=organ, type=u'0').delete()

    @classmethod
    def del_members(cls, organ):
        cls.objects.filter(organization=organ, type=u'1').delete()

    @classmethod
    def get_reviewers(cls, organ):
        reviewers = cls.objects.filter(organization=organ, type=u'0').all()
        ret = []
        for item in reviewers:
            ret.append(item.user)
        return ret

    @classmethod
    def get_members(cls, organ):
        members = cls.objects.filter(
            organization=organ, type=u'1').all()
        ret = []
        for item in members:
            ret.append(item.user)
        return ret


# ===============================================================================
# 奖项相关的表
# ===============================================================================
class LevelChoice(models.Model):
    level = models.CharField(u'奖项级别', max_length=20)

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
    apply_num = models.IntegerField(u"申报人数", default=0)
    awarded_num = models.IntegerField(u"获奖人数", default=0)
    pub_time = models.DateTimeField(u"申报时间", auto_now_add=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name
