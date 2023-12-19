'''Admin configuration for the fsm_website app.'''
from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    '''Admin View for Video'''
    list_display = ('url',)
    list_filter = ('url',)
    search_fields = ('url',)
    ordering = ('url',)


admin.site.register(Video, VideoAdmin)
