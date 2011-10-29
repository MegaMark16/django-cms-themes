VERSION = (1,0,5)
__version__ = "1.0.5"
import random 
import os

def init_themes():
    from django.contrib.sites.models import Site
    from cms.conf.patch import post_patch

    if not hasattr(settings, 'THEMES_DIR'):
        THEMES_DIR = os.path.join(settings.PROJECT_DIR, 'themes')
        if not os.path.exists(THEMES_DIR):
            os.makedirs(THEMES_DIR)
        settings.STATICFILES_DIRS = (
            ('themes', os.path.join(settings.PROJECT_DIR, "themes")),
        ) + settings.STATICFILES_DIRS
        setattr(settings, 'THEMES_DIR', THEMES_DIR)
    if not hasattr(settings, 'DEFAULT_CMS_TEMPLATES'):
        setattr(settings, 'DEFAULT_CMS_TEMPLATES', settings.CMS_TEMPLATES)
    if settings.THEMES_DIR not in settings.TEMPLATE_DIRS:
        settings.TEMPLATE_DIRS = settings.TEMPLATE_DIRS + (settings.THEMES_DIR,)

def set_themes():
    try:
        site = Site.objects.get(id=settings.SITE_ID)
        themes = [theme[0] for theme in site.theme_set.values_list('name')]
    except: 
        themes = []
    theme_templates = []
    
    for theme_dir in os.listdir(settings.THEMES_DIR):
        if theme_dir in themes or not themes:
            theme_full_path = os.path.join(settings.THEMES_DIR, theme_dir)
            if os.path.isdir(theme_full_path) and 'templates' in os.listdir(theme_full_path):
                template_path = os.path.join(theme_full_path, 'templates')
                for template in os.listdir(template_path):
                    template_path = os.path.join(theme_dir, 'templates', template)
                    template_display = '%s (%s)' % (template.replace('_', ' ').title().split('.')[0], theme_dir)
                    theme_templates.append((template_path, template_display))
    
    setattr(settings, 'CMS_TEMPLATES', tuple(theme_templates) + settings.DEFAULT_CMS_TEMPLATES)

try:
    from django.conf import settings
    init_themes()
    set_themes()
except ImportError:
    pass
