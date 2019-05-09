# -*- coding: utf-8 -*-
from system_management.models import OrganizationUser


def is_reviewer(self, user_qq):
    """
    是否负责人
    """
    if self.is_superuser:
        return True

    return OrganizationUser.objects.filter(
        user=user_qq, type=u'0').exists()