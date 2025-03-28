# Import necessary modules
from pathlib import Path
import environ

# Initialize environment variables using Django-environ
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

# Set the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Configure the secret key, debug mode, and allowed
# hosts from environment variables
SECRET_KEY = env('DJANGO_SECRET_KEY', default='din-default-hemlighet')
DEBUG = env('DJANGO_DEBUG', default=False)
ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS', default='localhost').split(',')

# Application definition: list of installed apps
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Custom apps
    'posts',
]

# Define tje middleware classes for request/response processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Set the root URL configuration module
ROOT_URLCONF = 'project_4.urls'

# Configure templates for the project
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

# Define the WSGI application for serving the project
WSGI_APPLICATION = 'project_4.wsgi.application'

# Configure the database settings using environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME', default='serious_talk.db'),
        'USER': env('DB_USER', default='user'),
        'PASSWORD': env('DB_PASSWORD', default='password'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432',)
    }
}

# Static files (CSS, Javascript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
