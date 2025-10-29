# app_cursos/models.py

from django.db import models

class Curso(models.Model):
    id_curso = models.CharField(max_length=10, primary_key=True, unique=True) # Un id único para el curso
    nombre_curso = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True) # blank=True permite que sea opcional en formularios
    duracion = models.CharField(max_length=50, help_text="Ej: '30 horas', '2 semanas'")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre_curso

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['nombre_curso'] # Ordena los cursos por nombre por defecto