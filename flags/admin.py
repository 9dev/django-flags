from django.contrib import admin

from .models import Approve, Flag


class FlagAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'creator', 'creation_date')
    actions = ['approve']

    def approve(self, request, queryset):
        for flag in queryset:
            Approve.objects.create(content_object=flag.content_object, creator=request.user)
        self.message_user(request, "Successfully approved selected objects.")


class ApproveAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'creator', 'creation_date')


admin.site.register(Flag, FlagAdmin)
admin.site.register(Approve, ApproveAdmin)
