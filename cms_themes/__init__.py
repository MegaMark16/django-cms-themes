VERSION = (1,0,9)
__version__ = "1.0.9"
import random
import os

def init_themes():
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
    if not hasattr(settings, 'DEFAULT_TEMPLATE_DIRS'):
        setattr(settings, 'DEFAULT_TEMPLATE_DIRS', settings.TEMPLATE_DIRS)
    if not hasattr(settings, 'DEFAULT_STATICFILES_DIRS'):
        setattr(settings, 'DEFAULT_STATICFILES_DIRS', settings.STATICFILES_DIRS)

def set_themes():
    if not Site.objects.filter(id=settings.SITE_ID):
        return

    site = Site.objects.get(id=settings.SITE_ID)
    themes = None

    if hasattr(site, 'theme_set'):
        try:
            themes = [theme.name for theme in site.theme_set.all()]
        except:
            pass

    if not themes:
        return

    theme_templates = []
    theme_static = []
    for theme_dir in os.listdir(settings.THEMES_DIR):
        if theme_dir in themes:
            theme_full_path = os.path.join(settings.THEMES_DIR, theme_dir)
            if os.path.isdir(theme_full_path) and 'templates' in os.listdir(theme_full_path):
                template_path = os.path.join(theme_full_path, 'templates')
                setattr(settings, 'TEMPLATE_DIRS', (template_path,) + settings.DEFAULT_TEMPLATE_DIRS)
                for template in os.listdir(template_path):
                    template_display = '%s (%s)' % (template.replace('_', ' ').title().split('.')[0], theme_dir)
                    theme_templates.append((template, template_display))

    setattr(settings, 'CMS_TEMPLATES', tuple(theme_templates) + settings.DEFAULT_CMS_TEMPLATES)
    setattr(settings, 'STATICFILES_DIRS', (settings.THEMES_DIR,) + settings.DEFAULT_STATICFILES_DIRS)

try:
    from django.conf import settings
    from django.contrib.sites.models import Site
    from cms.conf.patch import post_patch
    from cms_themes.models import Theme

    init_themes()
    set_themes()
except Exception as ex:
    print 'An error occured setting up the themes: %s' % ex

