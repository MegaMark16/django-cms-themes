from django.contrib import admin, messages
from models import Theme
from django.conf import settings
from django.utils.translation import ugettext, ugettext_lazy as _
from django.db import models

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id','name',)
    list_filter = ('name',)
    filter_horizontal = ('sites',)
    readonly_fields = ('name',)
admin.site.register(Theme, ThemeAdmin)

from cms.models import Page
from cms.admin.pageadmin import PageAdmin
from cms.admin.forms import PageAddForm,PageForm
admin.site.unregister(Page)
t = Page._meta.get_field_by_name("template")[0]
template_choices = [(x, _(y)) for x,y in settings.CMS_TEMPLATES]
t.choices.extend(template_choices)
admin.site.register(Page, PageAdmin)


