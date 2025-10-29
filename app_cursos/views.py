# app_cursos/views.py

from django.shortcuts import render
from .models import Curso # Importa el modelo Curso (lo crearemos en el paso 11)

def index(request):
    cursos = Curso.objects.all() # Obtiene todos los cursos de la base de datos
    context = {'cursos': cursos}
    return render(request, 'app_cursos/index.html', context) # Renderiza el template