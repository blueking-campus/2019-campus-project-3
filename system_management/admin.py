from django.contrib import admin
from .models import Organization
from .models import Award
from .models import OrganizationUser

# class OrganizationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'reviewer', 'staff', 'update_person', 'pub_time')
#
#
# class AwardAdmin(admin.ModelAdmin):
#     list_display = ('name', 'level', 'organization',
#                     'status', 'begin_time', 'pub_time', 'apply_num', 'awarded_num')


2

# Register your models here.
admin.site.register(Organization)
admin.site.register(OrganizationUser)
admin.site.register(Award)
