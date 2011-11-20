import tarfile
import StringIO
import shutil
import os

from django.conf import settings
from django.db import models
from django.contrib.sites.models import Site
from django.db.models.signals import post_save, pre_save, post_delete, m2m_changed
from cms_themes import set_themes

class Theme(models.Model):
    sites = models.ManyToManyField(Site, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    theme_file = models.FileField(upload_to='themes_archives', null=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            f = tarfile.open(fileobj=self.theme_file, mode='r:gz')
            self.name = f.getnames()[-1]
            f.extractall(settings.THEMES_DIR)

        super(Theme, self).save(*args, **kwargs)
                
    
    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"

    def __unicode__(self):
        return self.name

def delete_themes(sender, **kwargs):
    instance = kwargs['instance']
    try:
        shutil.rmtree(os.path.join(settings.THEMES_DIR, instance.name))
    except OSError: 
        pass
    set_themes()

def theme_site_m2m_changes(sender, **kwargs):
    instance = kwargs['instance']
    action = kwargs['action']
    if action in ("post_add", "post_remove", "post_clear"):
        if type(instance) is Theme:
            for site in instance.sites.all():
                for theme in site.theme_set.all():
                    if theme.id != instance.id:
                        site.theme_set.remove(theme)        
        set_themes()
post_delete.connect(delete_themes, sender=Theme)
m2m_changed.connect(theme_site_m2m_changes, sender=Theme.sites.through)
