from django.contrib import admin

from .models import Approve, Flag


class FlagAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'creator', 'creation_date')
    actions = ['delete_selected_flagged_objects', 'approve']

    def approve(self, request, queryset):
        for flag in queryset:
            Approve.objects.create(content_object=flag.content_object, creator=request.user)
        self.message_user(request, "Successfully approved selected objects.")

    def delete_selected_flagged_objects(self, request, queryset):
        for flag in queryset:
            flag.content_object.delete()
            flag.delete()
        self.message_user(request, "Successfully deleted selected flagged objects.")


class ApproveAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'creator', 'creation_date')


admin.site.register(Flag, FlagAdmin)
admin.site.register(Approve, ApproveAdmin)
