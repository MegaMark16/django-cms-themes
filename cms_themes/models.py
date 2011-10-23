import tarfile
import StringIO
import shutil
import os

from django.conf import settings
from django.db import models
from django.contrib.sites.models import Site
from django.db.models.signals import post_save, pre_save, post_delete
from cms_themes import set_themes

class Theme(models.Model):
    sites = models.ManyToManyField(Site, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    theme_file = models.FileField(upload_to='themes_archives', null=True)
    
    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"

    def __unicode__(self):
        return self.name

def extract_theme(sender, **kwargs):
    instance = kwargs['instance']
    if not instance.id:
        f = tarfile.open(fileobj=instance.theme_file, mode='r:gz')
        instance.name = f.getnames()[-1]
        f.extractall(settings.THEMES_DIR)
    set_themes()
    
def update_themes(sender, **kwargs):
    instance = kwargs['instance']
    shutil.rmtree(os.path.join(settings.THEMES_DIR, instance.name))
    set_themes()

pre_save.connect(extract_theme, sender=Theme)
post_delete.connect(update_themes, sender=Theme)

