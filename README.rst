django-cms-themes
=================
A django app that lets you load theme packs that are bundled templates, and select which theme a site should use.

Dependancies
============

- django (tested with 1.3)
- django-cms (tested with 2.2)

Getting Started
=============

To get started simply install using ``pip``:
::
    pip install django-cms-themes

Add ``cms_themes`` to your installed apps and ``syncdb`` (or migrate, if you have south installed).

Your installed apps should look something like this:
::
	INSTALLED_APPS = (
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.sites',
	    'django.contrib.messages',
	    'django.contrib.admin',
	    'cms',
	    'cms_themes',
	)
	
Make sure that you have a setting in your settings file called PROJECT_DIR that points to the root of your project, i.e. PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

Usage
=============

All usage is done through the admin.

Simply create a new Theme record and upload a theme tarball (tar.gz) file from http://www.djangocmsthemes.com.  All templates from themes uploaded should now show up in your Templates drop down on a django cms page.


