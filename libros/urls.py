from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import BibliotecaViewSet
from .views import mapa_bibliotecas

# Router crea automáticamente todas las rutas del ViewSet
router = DefaultRouter()
router.register(r'bibliotecas', BibliotecaViewSet, basename='biblioteca')

# Rutas generadas automáticamente:
# GET    /api/bibliotecas/
# POST   /api/bibliotecas/
# GET    /api/bibliotecas/1/
# PUT    /api/bibliotecas/1/
# DELETE /api/bibliotecas/1/
# GET    /api/bibliotecas/cercanas/?lat=14&lng=-87
# POST   /api/bibliotecas/1/geocodificar/

urlpatterns = [
    path('', include(router.urls)),
    path('mapa/', mapa_bibliotecas, name='mapa'),
]