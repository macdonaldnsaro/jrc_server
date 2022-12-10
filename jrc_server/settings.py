from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'nck%2=ml0p!eqjfmf0xxz$f^d5u@^!tli^dx%7o=3umji@u30('
DEBUG = True

ALLOWED_HOSTS = ["http://127.0.0.1:8000,http://127.0.0.1:8080"]

INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'django.contrib.humanize',

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    "authentication",
    "home",
    "corsheaders",

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


"rest_framework",
"audiofield",
]

MIDDLEWARE = [

    # 'whitenoise.middleware.WhiteNoiseMiddleware',
# 'django.middleware.gzip.GZipMiddleware',
#     'htmlmin.middleware.HtmlMinifyMiddleware',
#     'htmlmin.middleware.MarkRequestMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware',
    "audiofield.middleware.threadlocals.ThreadLocals"
]

ROOT_URLCONF = 'jrc_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'html')],
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

WSGI_APPLICATION = 'jrc_server.wsgi.application'



DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        },
     #    'default_read':  {
     #         'ENGINE': 'django.db.backends.sqlite3',
     #         'NAME': os.path.join(BASE_DIR, 'default.db.sqlite3')
     #    },
     #     'replica1':  {
     #         'ENGINE': 'django.db.backends.sqlite3',
     #         'NAME': os.path.join(BASE_DIR, 'users_db.db.sqlite3')
     #    },
     #     'replica2':  {
     #         'ENGINE': 'django.db.backends.sqlite3',
     #         'NAME': os.path.join(BASE_DIR, 'users_db.db.sqlite3')
     #    },
     #     'replica3':  {
     #         'ENGINE': 'django.db.backends.sqlite3',
     #         'NAME': os.path.join(BASE_DIR, 'users_db.db.sqlite3')
     #    },
     #     'replica4':  {
     #         'ENGINE': 'django.db.backends.sqlite3',
     #         'NAME': os.path.join(BASE_DIR, 'users_db.db.sqlite3')
     #    },
     #    'chat_db':  {
     #         'ENGINE': 'django.db.backends.sqlite3',
     #         'NAME': os.path.join(BASE_DIR, 'chat_db.db.sqlite3')
     #    } ,
     } 



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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

ALLOWED_HOSTS = ['*']
ALLOWED_SIGNUP_DOMAINS = ['*']

AUTH_USER_MODEL= 'authentication.User'


STATIC_URL = '../../../http:\/\/127.0.0.1:57476/static/'
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    BASE_DIR / "static",

]

STATIC_ROOT = str(BASE_DIR / "staticRoot",)

MEDIA_ROOT = BASE_DIR / 'media'
TEMP = BASE_DIR/'media/temp'

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient",'IGNORE_EXCEPTIONS': True,},
#         # "KEY_PREFIX": "example"
#     }
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': os.path.join(BASE_DIR, "CACHES"),
#         'TIMEOUT': 60,
#         'OPTIONS': {
#             'MAX_ENTRIES': 1000
#         }
#     }
# }


# CHANNEL_LAYERS={
#     'default': {
#         'BACKEND':'channels_redis.core.RedisChannelLayer',
#         'CONFIG':{
#             'hosts': [('localhost', 6379)],
#         }
#     },
# }

CHANNEL_LAYERS = {
    'default': {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
}}



EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'mail')
EMAIL_HOST='localhost'

BASE_URL='0.0.0.0:8000'
LOGIN_URL='/login/'


# DATA_UPLOAD_MAXMEMORY_SIZE = 10485760_000  # 10MB shall be the maximum size of a file upload in th esite to maximize storage


LOGIN_REDIRECT_URL = 'feeds'
LOGIN_URL = 'login'

# # PASSWORDS
# # ------------------------------------------------------------------------------
# # https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
#     # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    # 'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher','django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher','django.contrib.auth.hashers.BCryptSHA256PasswordHasher','django.contrib.auth.hashers.BCryptPasswordHasher',
]



############################################################################################3

# Frontend widget values
# 0-Keep original, 1-Mono, 2-Stereo
CHANNEL_TYPE_VALUE = 0

# 0-Keep original, 8000-8000Hz, 16000-16000Hz, 22050-22050Hz,
# 44100-44100Hz, 48000-48000Hz, 96000-96000Hz
FREQ_TYPE_VALUE = 8000

# 0-Keep original, 1-Convert to MP3, 2-Convert to WAV, 3-Convert to OGG
CONVERT_TYPE_VALUE = 0

FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'
