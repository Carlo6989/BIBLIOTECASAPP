from django.contrib import admin
from django.urls import path, include
from libros.views import mapa_bibliotecas

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración
    path('api/', include('libros.urls')),  # Tu API

   
    path('', mapa_bibliotecas, name='home'), 
]