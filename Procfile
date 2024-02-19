release: python manage.py migrate
web: waitress-serve --listen=*:8000 myapp.wsgi:application
worker: celery -A storefront worker
