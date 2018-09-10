
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', "mydb"),
        'USER': os.environ.get('USER_NAME', "root"),
        'PASSWORD': os.environ.get('PASSWORD', "root"),
        'HOST': os.environ.get('HOST_NAME', "localhost"),
        'PORT': os.environ.get('PORT', "3306"),
    }
}

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['corsheaders']

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True