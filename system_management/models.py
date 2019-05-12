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
        OrganizationUser.create_reviewers(list(set(data['reviewers'].split(';'))), obj)
        OrganizationUser.create_members(list(set(data['members'].split(';'))), obj)
        return obj

    @staticmethod
    def update_organization(obj, data, user):
        obj.name = data['name']
        obj.update_person = user
        obj.save()
        OrganizationUser.del_members(obj)
        OrganizationUser.del_reviewers(obj)
        OrganizationUser.create_reviewers(list(set(data['reviewers'].split(';'))), obj)
        OrganizationUser.create_members(list(set(data['members'].split(';'))), obj)


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
            'reviewers': ';'.join(OrganizationUser.get_reviewers(self)),
            'members': ';'.join(OrganizationUser.get_members(self)),
            'update_person': 'admin' if not self.update_person.get_full_name() else self.update_person.get_full_name(),
            'pub_time': self.pub_time.strftime("%Y-%m-%d %H:%M:%S"),
        }

    @staticmethod
    def to_array(organizations):
        data = []
        for item in organizations:
            data.append({
                'id': item.id,
                'name': item.name,
                'reviewers': ';'.join(OrganizationUser.get_reviewers(item)),
                'members': ';'.join(OrganizationUser.get_members(item)),
                'update_person': 'admin' if not item.update_person.get_full_name() else item.update_person.get_full_name(),
                'pub_time': item.pub_time.strftime("%Y-%m-%d %H:%M:%S"),
            })
        return data


class OrganizationUser(models.Model):
    """组织人员表"""
    organization = models.ForeignKey(Organization)
    user = models.CharField(max_length=20, verbose_name='人员qq号')
    TYPE_CHOICES = (
        (u'0', u'负责人员'),
        (u'1', u'参评人员'),
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.user

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
class Award(models.Model):
    name = models.CharField(u"申报奖项", max_length=255)
    requirement = models.TextField(u"评奖条件")
    LEVEL_CHOICES = (
        (u'0', u'小组级'),
        (u'1', u'部门级'),
        (u'2', u'中心级'),
        (u'3', u'公司级'),
    )
    level = models.CharField(u"奖项等级", max_length=1, choices=LEVEL_CHOICES)
    organization = models.ForeignKey(Organization, verbose_name=u"所属组织")
    begin_time = models.DateTimeField(u"开始日期", auto_now=True)
    end_time = models.DateTimeField(u"结束日期")
    STATUS_CHOICES = (
        (True, u'生效中'),
        (False, u'已过期'),
    )
    status = models.BooleanField(u"状态", choices=STATUS_CHOICES)
    appendix_status = models.BooleanField(u"附件状态", default=False)
    # TODO: appendix
    pub_time = models.DateTimeField(u"申报时间", auto_now_add=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name

    @property
    def apply_count(self):
        from personal_center.models import Apply
        return Apply.objects.filter(award=self).count()

    @property
    def apply_all(self):
        from personal_center.models import Apply
        return Apply.objects.filter(award=self)

    @property
    def awarded_count(self):
        from personal_center.models import Apply
        return Apply.objects.filter(award=self, status=u'3').count()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'requirement': self.requirement,
            'reviewers': self.organization.to_json()['reviewers'],
            'status': self.get_status_display(),
            'level': self.get_level_display(),
            'organization': self.organization.name,
            'begin_time': self.begin_time,
            'end_time': self.end_time,
            'apply_all': self.apply_all
        }
