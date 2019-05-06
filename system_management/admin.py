from django.contrib import admin
from .models import Organization
from .models import Openid2qq
from .models import Award


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'reviewer', 'staff', 'update_person', 'pub_time')


class AwardAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'organization',
                    'status', 'begin_time', 'pub_time', 'apply_num', 'awarded_num')


# Register your models here.
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Openid2qq)
admin.site.register(Award, AwardAdmin)
