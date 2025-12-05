from django.shortcuts import render
from .tasks import descargar_audio

# mensajes django
from django.contrib import messages


# Create your views here.
def index_function(request):
    if request.method == "POST":
        url = request.POST.get("url")
        nombre = request.POST.get("nombre")
        if url and nombre:
            # Llamar a la tarea Celery para descargar el audio
            descargar_audio.delay(url, nombre)
            messages.success(request, "Descarga en progreso...")
            return render(request, "home.html")
        else:
            messages.error(request, "Por favor, complete todos los campos.")
            return render(request, "home.html")
        # return render(request, 'download.html')
    return render(request, "home.html")
