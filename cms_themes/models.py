from django.conf import settings
from django.db import models
from django.contrib.sites.models import Site
from django.db.models.signals import post_save, pre_save
import tarfile
import StringIO

class Theme(models.Model):
    sites = models.ManyToManyField(Site, null=True, blank=True)
    name = models.CharField(max_length=255)
    theme_file = models.FileField(upload_to='themes_archives', null=True)
    
    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"

def extract_theme(sender, **kwargs):
    instance = kwargs['instance']
    if not instance.id:
        print dir(instance.theme_file)
        f = tarfile.open(fileobj=instance.theme_file, mode='r:gz')
        f.extractall(settings.THEMES_DIR)
    
pre_save.connect(extract_theme, sender=Theme)

