from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

import reversion

from congregation_portal import models as shared_models
from territory import models as territory_models


class ProfileInline(admin.StackedInline):
    model = shared_models.Profile
    can_delete = False
    verbose_name = "User Profile"


class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )


class CongregationAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'city', 'state']
    sortable_field_name = ['id', 'name']


class TerritoryItemInline(admin.StackedInline):
    model = territory_models.TerritoryItem
    can_delete = True
    verbose_name = "Territory Item"


class TerritoryAdmin(reversion.VersionAdmin):
    inlines = (TerritoryItemInline, )
    verbose_name = "Territory"


reversion.register(territory_models.Territory, follow=("territoryitem_set",))
reversion.register(territory_models.TerritoryItem, follow=("territory",))

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(shared_models.Congregation, CongregationAdmin)

admin.site.register(territory_models.Territory, TerritoryAdmin)
