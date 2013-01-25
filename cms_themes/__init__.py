VERSION = (1,0,10)
__version__ = "1.0.10"
import random
import os
import imp
import sys

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
    # update SITE_ALIASES
    SITE_ALIASES = getattr(settings, "SITE_ALIASES", {})
    for theme_dir in os.listdir(settings.THEMES_DIR):
        try:
            theme = Theme.objects.get(name=theme_dir)
            SITE_ALIASES['%s.127.0.0.1.xip.io' % theme.name] = theme.sites.all()[0].domain
        except:
            continue
    setattr(settings, 'SITE_ALIASES', SITE_ALIASES)


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
            if os.path.isdir(theme_full_path):
                if 'templates' in os.listdir(theme_full_path):
                    # handle templates
                    template_path = os.path.join(theme_full_path, 'templates')
                    setattr(settings, 'TEMPLATE_DIRS', (template_path,) + settings.DEFAULT_TEMPLATE_DIRS)
                    for template in os.listdir(template_path):
                        if '.' not in template:
                            continue # skip directories
                        template_display = '%s (%s)' % (template.replace('_', ' ').title().split('.')[0], theme_dir)
                        theme_templates.append((template, template_display))
                for file in os.listdir(theme_full_path):
                    # handle settings
                    # inspired by http://passingcuriosity.com/2010/default-settings-for-django-applications/
                    if ('settings' in file or 'conf' in file) and file.endswith('.py'):
                        module = file.split('.py')[0]
                        try:
                            theme_settings = imp.load_source(module,
                                os.path.join(theme_full_path, file)
                            )
                            _def_settings = sys.modules['django.conf.global_settings']
                            for key in dir(theme_settings):
                                if key.startswith('_'):
                                    continue
                                setattr(settings, key, getattr(theme_settings, key))
                        except IOError:
                        # This theme doesn't exist or doesn't have a settings file
                            pass

    setattr(settings, 'CMS_TEMPLATES', tuple(theme_templates) + settings.DEFAULT_CMS_TEMPLATES)
    setattr(settings, 'STATICFILES_DIRS', (settings.THEMES_DIR,) + settings.DEFAULT_STATICFILES_DIRS)

try:
    from django.conf import settings
    from django.contrib.sites.models import Site
    from cms.conf.patch import post_patch
    from cms_themes.models import Theme

    init_themes()
    set_themes()
except Exception, ex:
    print 'An error occured setting up the themes: %s' % ex

