# -*- coding: utf-8 -*-
"""
Django settings for autolavadox project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yup+#q@+j!^gt9oi=wal33n#0n4)t(j19d6fz97a*91_v@*4$^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost','http://luxuryservice.com.co'
]

EXILE_UI = {
    'site_title': 'LavaAutox',
    'site_header': 'LavaAutox',
    'index_title': 'Software para lavaautos',
    'dash_template': 'admin/dash/newdash.html',
    'media': {
        'logo': {
            'dashboard': '/media/logo/carrito_mojado.svg',
            'page': '/media/logo/carrito_mojado.svg',
            'login': '/media/logo/carrito_mojado.png'
        },
        'icons': {
            'empleados': {
                'icon': 'people',
                'groups': [
                    'Empleado'
                ],
                'models': {
                    'Empleado': {'icon': 'people', 'group': 'Empleado'},
                    'Cajero': {'icon': 'people', 'group': 'Empleado'},
                    'Recepcionista': {'icon': 'people', 'group': 'Empleado'},

                },
            },
            'cliente': {
                'icon': 'person',
                'group': [
                    'Cliente'
                ],
                'models': {
                    'Cliente': {'icon': 'person', 'group': 'Cliente'},
                    'TipoVehiculo': {'icon': 'settings', 'group': 'Cliente'},
                    'Vehiculo': {'icon': 'directions_car', 'group': 'Cliente'}
                }
            },
            'operacion': {
                'icon': 'local_car_wash',
                'groups': [
                    'Operacion'
                ],
                'models': {
                    'TipoServicio': {'icon': 'settings', 'group': 'Operacion'},
                    'Servicio': {'icon': 'build', 'group': 'Operacion'},
                    'Orden': {'icon': 'assignment', 'group': 'Operacion'}
                },
            },
            'estadistica': {
                'icon': 'show_chart',
                'groups': [
                    'LocalEstadistica'
                ],
                'models': {
                    'TiemposOrden': {'icon': 'alarm_on', 'group': 'LocalEstadistica'}
                },
            },
            'auth': {
                'icon': 'security',
                'groups': [
                    'Seguridad',
                ],
                'models': {
                    'Group': {'icon': 'people', 'group': 'Seguridad'},
                    'User': {'icon': 'person', 'group': 'Seguridad'}
                }
            },
            'logout': {
                'icon': 'exit_to_app',
            }
        }
    }
}

MENU_ORDER = [
    {
        'name': 'empleados',
        'models': [
            'Empleado',
            'Recepcionista',
            'Cajero'
        ]
    },
    {
        'name': 'cliente',
        'models': [
            'Cliente',
            'TipoVehiculo',
            'Vehiculo'
        ]
    },
    {
        'name': 'operacion',
        'models': [
            'TipoServicio',
            'Servicio',
            'Orden'
        ]
    },
    {
        'name': 'estadistica',
        'models': [
            'TiemposOrden'
        ]
    },
    {
        'name': 'auth',
        'models': [
            'Group',
            'User'
        ]
    },
    {
        'name': 'logout'
    }
]


# Application definition

INSTALLED_APPS = [
    'exileui',
    'informes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nested_admin',
    'django_select2',
    'daterange_filter',
    'supra',
    'empleados.apps.EmpleadosConfig',
    'cliente.apps.ClienteConfig',
    'operacion.apps.OperacionConfig',
    'interface',
    'import_export',
    'estadistica'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'autolavadox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'autolavadox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lavado2',
        'USER': 'postgres',
        'PASSWORD': 'Exile*74522547',
        'HOST': '104.236.33.228',
        'POST': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
HOST_MEDIA = 'http://luxuryservice.com.co/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
