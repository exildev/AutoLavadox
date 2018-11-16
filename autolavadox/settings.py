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
SERVER_STATIC='http://ec2-184-73-84-219.compute-1.amazonaws.com:8030'
SERVER_M='http://ec2-184-73-84-219.compute-1.amazonaws.com:8030'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&up7i-+v$lvt_s5^@c63f@jwp)ddr8=qqh*b9_nqs2pxr25ytz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost', '*','http://ec2-184-73-84-219.compute-1.amazonaws.com','https://storage.googleapis.com'
]

EXILE_UI = {
    'site_title': 'Exile Cars Service',
    'site_header': 'Exile Cars Service',
    'index_title': 'Exile Cars Service',
    'dash_template': 'admin/dash/newdash.html',
    'media': {
        'logo': {
            'dashboard': '{}/media/logo/carrito_mojado.svg'.format(SERVER_STATIC),
            'page': '{}/media/logo/carrito_mojado.svg'.format(SERVER_STATIC),
            'login': '{}/media/logo/carrito_mojado.png'.format(SERVER_STATIC)
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
                    'Orden': {'icon': 'assignment', 'group': 'Operacion'},
                    'ComposicionServicio': {'icon': 'build', 'group': 'Operacion'},
                    'Componente': {'icon': 'move_to_inbox', 'group': 'Operacion'},
                    'HistoriaDeServicioVenta': {'icon': 'move_to_inbox', 'group': 'Operacion'},
                    'HistoriaDeServicioOperacion': {'icon': 'move_to_inbox', 'group': 'Operacion'}
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
                    'Subcripcion'
                ],
                'models': {
                    'Cuenta': {'icon': 'move_to_inbox', 'group': 'Subcripcion'},
                    'Cliente': {'icon': 'move_to_inbox', 'group': 'Subcripcion'},
                    'Funcionalidad': {'icon': 'move_to_inbox', 'group': 'Subcripcion'},
                    'Modulo': {'icon': 'move_to_inbox', 'group': 'Subcripcion'},
                    'InstModulo': {'icon': 'move_to_inbox', 'group': 'Subcripcion'},
                    'Plan': {'icon': 'move_to_inbox', 'group': 'Subcripcion'},
                    'Suscripcion': {'icon': 'move_to_inbox', 'group': 'Subcripcion'},
                    'Factura': {'icon': 'move_to_inbox', 'group': 'Subcripcion'},
                },
            },
            'inventario': {
                'icon': 'storage',
                'groups': [
                    'Inventario'
                ],
                'models': {
                    'Presentacion': {'icon': 'move_to_inbox', 'group': 'Inventario'},
                    'Producto': {'icon': 'move_to_inbox', 'group': 'Inventario'},
                    'Venta': {'icon': 'move_to_inbox', 'group': 'Inventario'},
                    'Operacion': {'icon': 'extension', 'group': 'Inventario'},
                    'Cierre': {'icon': 'extension', 'group': 'Inventario'},
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
            'Orden',
            'ComposicionServicio',
            'Componente',
            'HistoriaDeServicioVenta',
            'HistoriaDeServicioOperacion',
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
        'name': 'inventario',
        'models': [
            'Presentacion',
            'Producto',
            'Venta',
            'Operacion',
            'Cierre',
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
    'django.contrib.humanize',
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
    'easy_select2',
    'inventario',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
'cuser.middleware.CuserMiddleware',
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
        #'HOST': 'ec2-184-73-84-219.compute-1.amazonaws.com',
        #'USER': 'epic',
        'USER': 'postgres',
        #'PASSWORD': '123456',
        'PASSWORD': '85412369**$%%&*(/%$#qazxswEDC',
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
"""
STATIC_URL = '/static/'
STATIC_ROOT = '/home/dark/practicas/AutoLavadox/static'
MEDIA_URL = '/media/'
HOST_MEDIA = '/home/dark/practicas/AutoLavadox/media'
MEDIA_ROOT = '/home/dark/practicas/AutoLavadox/media'
LOGOUT_URL = '/accounts/login/'
SERVER_STATIC = ''
SERVER_M = ''

"""
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/AutoLavadox/static'
MEDIA_URL = '/media/'
HOST_MEDIA = '/media/'
MEDIA_ROOT = '/var/www/AutoLavadox/media'
LOGOUT_URL = '/accounts/login/'

