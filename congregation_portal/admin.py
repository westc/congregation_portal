from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from congregation_portal import models as shared_models


class ProfileInline(admin.StackedInline):
    model = shared_models.Profile
    can_delete = False
    verbose_name = "User Profile"


class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )


class CongregationAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'city', 'state']
    sortable_field_name = ['id', 'name']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(shared_models.Congregation, CongregationAdmin)