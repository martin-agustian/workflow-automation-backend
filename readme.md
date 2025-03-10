## Step 1: Set Up Database Configuration in settings.py :
Here is my default config
```bash
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
```
you can modify it based on your default connection in settings.py

## Step 2: Run Migrations :
1. Run "python manage.py makemigrations" on terminal to create migration file
2. Run "python manage.py migrate" on terminal to create migration table and structure in database

## STEP 3 Setup Zapier :
you can watch this video i made https://www.youtube.com/watch?v=YEteyFTYxtY (if you need indonesian version for better understanding, contact me via email martinagustian@yahoo.com)

## Step 4: Update the Zapier URL :
1. Rename .env.example to .env
2. Set the ZAPIER_URL value to your Zapier webhook URL

## STEP 5 Run Project :
Run "python manage.py runserver" on terminal