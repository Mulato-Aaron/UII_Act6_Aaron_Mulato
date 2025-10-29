# backend_preparatoria/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/', include('app_cursos.urls')),
    path('', include('app_cursos.urls')), # ¡Añade esta línea! Esto hará que la raíz '/' muestre lo mismo que '/cursos/'
]