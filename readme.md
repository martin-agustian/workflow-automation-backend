STEP 1 Setup DB Config in settings.py :
// Here is my config, you can change based on your default connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STEP 2 Run Migration :
python manage.py makemigrations
python manage.py migrate

STEP 3 Run Project :
python manage.py runserver