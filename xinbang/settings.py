# -*- coding: utf-8 -*-
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
"""
Django settings for xinbang project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-rj(y$3gv0eg_v!784xq7y&0bj+yc_)c3u1%3)_sr_!^$@-dyx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'ckeditor',
    'mptt',
    'page',
    'post',
    'menu',
    'util',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.i18n',
    'menu.processor.get_menu',
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)
ROOT_URLCONF = 'xinbang.urls'

WSGI_APPLICATION = 'xinbang.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'xinbang',
        'USER': 'jazdelu',
    'PASSWORD':'lushizhao1129',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'新邦集团官网后台管理系统',
    'HEADER_DATE_FORMAT': 'Y-m-d',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'MENU':(
        {'app':'auth','label':'User','icon':'icon-user'},
        {'app':'post','label':u'文章','icon':'icon-leaf'},
        {'app':'page','label':u'页面','icon':'icon-leaf'},
        {'app':'menu','label':u'菜单','icon':'icon-leaf'},
        {'app':'util','label':u'其他内容','icon':'icon-leaf'},
        {'label': u'首页', 'icon':'icon-leaf', 'url': '/'},
    ),
    # 'SEARCH_URL': '/admin/auth/user/',

    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # misc
    'LIST_PER_PAGE': 10
}
CKEDITOR_UPLOAD_PATH = "post/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [      'Undo', 'Redo',
              '-', 'Font','FontSize',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'Link', 'Unlink', 'Anchor',
              '-', 'Format',
            ],
            [ 
                   'BulletedList', 'NumberedList',
              '-', 'JustifyLeft','JustifyRight','JustifyCenter','JustifyBlock',
              '-', 'Cut','Copy','Paste','PasteText',
              '-', 'Source',
            ],
            [      
              '-', 'Image','Table','HorizontalRule','SpecialChar','PageBreak',
            ],
        ],
        'width': 840,
        'height': 300,
        'skin':'moono',
        'toolbarCanCollapse': False,
        'extraPlugins' : 'justify',
    }
}