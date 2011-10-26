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

Usage
=============

All usage is done through the admin.

Simply create a new Theme record and upload a theme tarball (tar.gz) file from djangocmsthemes.com.  All templates from themes uploaded should now show up in your Templates drop down on a django cms page.


Here are some example themes: 

http://www.ransomsoft.com/themes/red.tar.gz

http://www.ransomsoft.com/themes/simple.tar.gz

http://www.ransomsoft.com/themes/summer.tar.gz

http://www.ransomsoft.com/themes/blankandwhite.tar.gz

