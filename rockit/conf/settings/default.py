import os
import datetime

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Default security key

SECRET_KEY = 'e04#=m)0nv#^$0z+m#cf2+bm#4y^6se_e%!fm(k+_1#&wiqm2y'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'compressor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'django_jenkins',
    'djangobower',
    'corsheaders',
    'rest_framework',
    'rockit.core',
    'rockit.plugins.mailout',
    'rockit.plugins.picamera',
    'rockit.plugins.razberry',
    'rockit.plugins.astral',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

COMPRESS_PRECOMPILERS = (
   ('text/less', 'lessc {infile} {outfile}'),
)

INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'rockit.urls'

WSGI_APPLICATION = 'rockit.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True
#CORS_ORIGIN_WHITELIST = ('localhost:9000')

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "rockit.sqlite3"),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL  = '/static/'

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "bower_components"),
)

COMPRESS_ROOT = 'static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

JENKINS_TASKS = ('django_jenkins.tasks.django_tests',)
TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'
PROJECT_APPS = [appname for appname in INSTALLED_APPS if appname.startswith('rockit')]

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'rockit': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}
