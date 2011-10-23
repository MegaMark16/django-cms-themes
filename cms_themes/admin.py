from django.contrib import admin, messages
from models import Theme
from django.conf import settings

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id','name',)
    list_filter = ('name',)
    filter_horizontal = ('sites',)
    readonly_fields = ('name',)
admin.site.register(Theme, ThemeAdmin)

