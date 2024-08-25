INSTALLED_APPS = [
    # other apps
    'rest_framework',
    'corsheaders',
    'vulnerability_management',
    'drf_yasg',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # other middleware
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vulnerability_management',  # my database name
        'USER': 'vulnerability_management',  # my database user
        'PASSWORD': 'Blessing@123',  # my database password
        'HOST': 'localhost',
        'PORT': '5432',  # Default PostgreSQL port
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
