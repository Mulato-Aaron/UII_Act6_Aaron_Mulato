# app_cursos/admin.py

from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_curso', 'nombre_curso', 'duracion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre_curso', 'descripcion')
    list_filter = ('fecha_inicio', 'duracion')