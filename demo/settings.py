# Django settings for demo project.
import os
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

gettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'demo.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*^aor)8+d(lg_#ezg0&8sc&&pju^18#t=clw-2ief&q#+%(s*n'

LANGUAGE_CODE = 'en'

CMS_TEMPLATES = (
		('home.html', gettext('Homepage')),
)

CMS_PLACEHOLDER_CONF = {
    'footer-address-content': {
        'plugins': ('TextPlugin',),
        'name':gettext('Footer Link List'),
    },
    'footer-link-list': {
        'plugins': ('FilerImagePlugin',),
        'name':gettext('Footer Link List'),
    },
    'right-image': {
        'plugins': ('FilerImagePlugin',),
        'name':gettext('Right Image'),
    },
}

LANGUAGES = (
        ('en', gettext('English')),
)

CMS_LANGUAGES = LANGUAGES

GOOGLE_MAPS_API_KEY = ""

CMS_SHOW_END_DATE = True
CMS_SHOW_START_DATE = True
CMS_PERMISSION = True
CMS_MODERATOR = False
CMS_URL_OVERWRITE = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_SEO_FIELDS = True
CMS_REDIRECTS = True
CMS_SOFTROOT = True

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS" : False,
}

# Allowed IPs for the Django Debug Toolbar
INTERNAL_IPS = ('127.0.0.1',)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        "django.core.context_processors.auth",
        'django.core.context_processors.debug',
        "django.core.context_processors.i18n",
        "django.core.context_processors.request",
        "django.core.context_processors.media",
        "cms.context_processors.media",
        'django.contrib.messages.context_processors.messages',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
)

ROOT_URLCONF = 'demo.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	os.path.join(PROJECT_DIR,'templates'),
	os.path.join(PROJECT_DIR,'themes'),
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, "fixtures"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'cms',
    'menus',
    'cms.plugins.text',
    'mptt',
    'publisher',
    'south',
    'appmedia',
    'cms_themes',
)


SOUTH_TESTS_MIGRATE = False

try:
    from settings_dev import *
except ImportError:
    pass
