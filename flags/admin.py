from django.contrib import admin

from .models import Approve, Flag


class FlagAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'creator', 'creation_date')


class ApproveAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'creator', 'creation_date')


admin.site.register(Flag, FlagAdmin)
admin.site.register(Approve, ApproveAdmin)
