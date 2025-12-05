import os
from celery import Celery

# Establece el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ytapp.settings")

app = Celery("ytapp")

# Lee la configuración desde settings.py con el prefijo CELERY_
app.config_from_object("django.conf:settings", namespace="CELERY")

# Descubre automáticamente las tareas en todas las apps
app.autodiscover_tasks()
