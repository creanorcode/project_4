# Import necessary modules
from pathlib import Path
import environ
import dj_database_url

# ------------------------------------------------
# BASE DIRECTORY
# ------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------
# ENVIRONMENT VARIABLES (two-step overlay)
# ------------------------------------------------
env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    USE_PRODUCTION_ENV=(bool, False),
)

# 1) Load base .env if it exits
base_env_file = BASE_DIR / '.env'
if base_env_file.exists():
    env.read_env(env_file=base_env_file)

# 2) If USE_PRODUCTION_ENV=True, overlay with .env.production
if env.bool('USE_PRODUCTION_ENV'):
    prod_env_file = BASE_DIR / '.env.production'
    if prod_env_file.exists():
        env.read_env(env_file=prod_env_file)
    else:
        raise FileNotFoundError(
            f"Production env file not found: {prod_env_file}"
        )

# -------------------------------------------------------
# CORE SETTINGS
# -------------------------------------------------------
# Configure the secret key, debug mode, and allowed
# hosts from environment variables
SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env('DJANGO_DEBUG')
ALLOWED_HOSTS = (
    env.list(
        'DJANGO_ALLOWED_HOSTS',
        default=[
            'serioustalk-version1-52554b996a26.herokuapp.com',
            'serioustalk.eu',
            'www.serioustalk.eu',
        ]
    )
)

# -----------------------------------------------
# APPLICATION DEFINITION: list of installed apps
# -----------------------------------------------
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Custom apps
    'posts',
]
SITE_ID = 1

# -------------------------------------------------------------------------
# DJANGO_ALLAUTH - LOGIN, REGISTER, SOCIAL-LOGIN, EMAIL-VERIFICATION
# --------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # default
    'allauth.account.auth_backends.AuthenticationBackend',  # django-allauth
]

# --------------------------------------------------------------
# DJANGO-ALLAUTH CONFIGURATION
# --------------------------------------------------------------
ACCOUNT_SIGNUP_FIELDS = ['username*', 'email*', 'password1*', 'password2*']
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_METHODS = {'username', 'email'}
ACCOUNT_RATE_LIMITS = {
    # 10 per minute per IP, and 5 per 5 minutes per key
    'login_failed': "10/m/ip,5/5m/key",
}

# ---------------------------------------------------------------
# EMAIL (SMTP) CONFIGURATION
# ---------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default='smtp.strato.com')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
DEFAULT_FROM_EMAIL = env(
    'DEFAULT_FROM_EMAIL', default='no-reply@serioustalk.eu'
)

# ----------------------------------------------------------------------
# OTHER SETTINGS SUCH AS DATABASE CONFIGURATION, MIDDLEWARE, TEMPLATES, ETC.
# ----------------------------------------------------------------------
# Define the middleware classes for request/response processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # server static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # django-allauth needs this:
    'allauth.account.middleware.AccountMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Set the root URL configuration module
ROOT_URLCONF = 'project_4.urls'

# Configure templates for the project
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # global templates folder
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

# Define the WSGI application for serving the project
WSGI_APPLICATION = 'project_4.wsgi.application'

# ------------------------------------------------------------
# DATABASE
# ------------------------------------------------------------
# Configure the database settings using environment variables
DATABASES = {
    'default': dj_database_url.config(
        default=env(
            'DATABASE_URL',
            default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
        )
    )
}

# ---------------------------------------------------------
# AUTHENTICATION & PASSWORD VALIDATION (you can leave these as the default)
# ---------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        ),
    },
]

# -----------------------
# INTERNATIONALIZATION
# -----------------------
LANGUAGE_CODE = 'sv-se'
TIME_ZONE = 'Europe/Stockholm'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ---------------------------------------
# STATIC FILES (CSS, Javascript, Images)
# ---------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']  # your static source folder
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
WHITENOISE_MANIFEST_STRICT = False

# ----------------------------------------
# MEDIA FILES (User uploads)
# ----------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# ----------------------------------------
# SECURITY
# ----------------------------------------
# Trust the x-Forwarded-Proto header from you proxy (Heroku, ELB etc.)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = env.list(
    'CSRF_TRUSTED_ORIGINS',
    default=[
        'https://serioustalk.eu',
        'https://www.serioustalk.eu',
    ]
)

# Safety against XSS and content sniffing
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
# Prevent pages from being embedded in <iframe>
X_FRAME_OPTIONS = 'SAMEORIGIN'
# Force HTTPS (used in production) and Cookies only over HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000  # One year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# ----------------------------------------------
# CACHING
# ----------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# ------------------------------------------------------------------------------
# EMAIL
# ------------------------------------------------------------------------------
# EMAIL_BACKEND = env(
#     'EMAIL_BACKEND',
#     default='django.core.mail.backends.console.EmailBackend'
# )
# EMAIL_HOST = env('EMAIL_HOST', default='smtp.sendgrid.net')
# EMAIL_PORT = env.int('EMAIL_PORT', default=587)
# EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')
# EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
# DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='webmaster@localhost')

# ------------------------------------------------------------------------------
# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {
        'handlers': ['console'],
        'level': env('DJANGO_LOG_LEVEL', default='WARNING'),
    },
}

# ------------------------------------------------------------------------------
# LOGOUT & LOGIN DIRECTION
# ------------------------------------------------------------------------------
# Redirect users to the homepage after they log out
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'

# ------------------------------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# ------------------------------------------------------------------------------
# Add DEFAULT_AUTO_FIELD at the end of the file
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
