VERSION = (1,0,0)
__version__ = "1.0.0"
import random 
import os

from django.conf import settings
from django.contrib.sites.models import Site

PROJECT_DIR = settings.PROJECT_DIR
CMS_TEMPLATES = getattr(settings, 'CMS_TEMPLATES', ())

if hasattr(settings, 'THEMES_DIR'):
    THEMES_DIR = settings.THEMES_DIR
else:
    THEMES_DIR = os.path.join(PROJECT_DIR, 'themes')
    setattr(settings, 'THEMES_DIR', THEMES_DIR)
    
class cms_templates_iterable(object):
    def __iter__(self):
        return iter(self.get_themes())
    def __len__(self):
        return len(self.get_themes())
    def __getitem__(self, index):
        return self.get_themes()[index]
        
    def get_themes(self):
        try:
            site = Site.objects.get(id=settings.SITE_ID)
            themes = [theme[0] for theme in site.theme_set.values_list('name')]
        except: 
            themes = []
        theme_templates = []
        
        for theme_dir in os.listdir(THEMES_DIR):
            if theme_dir in themes or not len(themes):
                theme_full_path = os.path.join(THEMES_DIR, theme_dir)
                if 'templates' in os.listdir(theme_full_path):
                    template_path = os.path.join(theme_full_path, 'templates')
                    for template in os.listdir(template_path):
                        theme_templates.append((os.path.join(theme_dir, 'templates', template), '%s (%s)' % (template, theme_dir)))
        return theme_templates
setattr(settings, 'CMS_TEMPLATES', cms_templates_iterable())
