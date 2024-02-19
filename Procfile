release: python manage.py migrate
worker: celery -A storefront worker
web: waitress-serve --port=$PORT website:app