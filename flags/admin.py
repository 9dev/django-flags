from django.contrib import admin

from .models import Flag


class FlagAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'creator', 'creation_date')


admin.site.register(Flag, FlagAdmin)
