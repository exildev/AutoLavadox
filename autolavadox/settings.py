"""
Django settings for Autolavadox project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&up7i-+v$lvt_s5^@c63f@jwp)ddr8=qqh*b9_nqs2pxr25ytz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost', '*','https://www.autolavadox.appspot.com','https://storage.googleapis.com'
]

EXILE_UI = {
    'site_title': 'Exile Cars Service',
    'site_header': 'Exile Cars Service',
    'index_title': 'Exile Cars Service',
    'dash_template': 'admin/dash/newdash.html',
    'media': {
        'logo': {
            'dashboard': 'https://storage.googleapis.com/autolavadox/media/logo/carrito_mojado.svg',
            'page': 'https://storage.googleapis.com/autolavadox/media/logo/carrito_mojado.svg',
            'login': 'https://storage.googleapis.com/autolavadox/media/logo/carrito_mojado.png'
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
                    'Administrador': {'icon': 'people', 'group': 'Empleado'},

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
            'cierre': {
                'icon': 'attach_money',
                'groups': [
                    'Cierre'
                ],
                'models': {
                    'TipoServicio': {'icon': 'move_to_inbox', 'group': 'Cierre'},
                    'Factura': {'icon': 'move_to_inbox', 'group': 'Cierre'},
                    'Turno': {'icon': 'move_to_inbox', 'group': 'Cierre'},
                    'Cierre': {'icon': 'move_to_inbox', 'group': 'Cierre'}
                },
            },
            'subcripcion': {
                'icon': 'attach_money',
                'groups': [
                    'subcripcion'
                ],
                'models': {
                    'Cuenta': {'icon': 'move_to_inbox', 'group': 'Cierre'},
                    'Cliente': {'icon': 'move_to_inbox', 'group': 'Cierre'},
                    'Funcionalidad': {'icon': 'move_to_inbox', 'group': 'Cierre'},
                    'Modulo': {'icon': 'move_to_inbox', 'group': 'Cierre'},
                    'InstModulo': {'icon': 'move_to_inbox', 'group': 'Cierre'},
                    'Plan': {'icon': 'move_to_inbox', 'group': 'Cierre'},
                    'Suscripcion': {'icon': 'move_to_inbox', 'group': 'Cierre'},
                    'Factura': {'icon': 'move_to_inbox', 'group': 'Cierre'},
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
            'Cajero',
            'Administrador'
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
        'name': 'cierre',
        'models': [
            'TipoServicio',
            'Factura',
            'Turno',
            'Cierre'
        ]
    },
    {
        'name': 'subcripcion',
        'models': [
            'Cuenta',
            'Cliente',
            'Funcionalidad',
            'Modulo',
            'InstModulo',
            'Plan',
            'Suscripcion',
            'Factura',
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
    'xhtml2pdf',
    'empleados.apps.EmpleadosConfig',
    'cliente.apps.ClienteConfig',
    'operacion.apps.OperacionConfig',
    'interface',
    'import_export',
    'estadistica',
    'cierre',
    'subcripcion',
    'django_user_agents',
    'cuser',
    'autolavadox',
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
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'autolavadox',
        'HOST' :'localhost',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'POST': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-la'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/coviyarce/webapps/static_autolavadox'
MEDIA_URL = '/media/'
HOST_MEDIA = '/media/'
MEDIA_ROOT = '/home/coviyarce/webapps/media_autolavadox'
LOGOUT_URL = '/accounts/login/'