release: python manage.py makemigrations routes && python manage.py migrate
web: gunicorn call_routing.wsgi
