from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(SomeAbstractModel)
admin.site.register(NewsFeeds)
admin.site.register(Sermons)
admin.site.register(SermonAttendance)
admin.site.register(Announcements)
admin.site.register(Testimonies)
admin.site.register(Album)


class MessageAdmin(admin.ModelAdmin):
    list_filter = [
    ]
    list_display = [
    		"audio_file_player"
    ]
    actions = ['custom_delete_selected']
    def custom_delete_selected(self, request, queryset):
    #custom delete code
	    n = queryset.count()
	    for i in queryset:
	        if i.audio_file:
	            if os.path.exists(i.audio_file.path):
	                os.remove(i.audio_file.path)
	        i.delete()
	    self.message_user(request, ("Successfully deleted %d audio files.") % n)
    custom_delete_selected.short_description = "Delete selected items"

    def get_actions(self, request):
	    actions = super(AudioFileAdmin, self).get_actions(request)
	    del actions['delete_selected']
	    return actions


admin.site.register(AudioSermon,MessageAdmin)
