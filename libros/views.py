from django.shortcuts import render
import os
from dotenv import load_dotenv # Asegúrate de tener python-dotenv instalado

load_dotenv() # Carga las variables del archivo .env

def mapa_bibliotecas(request):
    """
    Vista que muestra el mapa de bibliotecas con la API Key cargada
    """
    context = {
        'google_maps_api_key': os.getenv('GOOGLE_MAPS_API_KEY')
    }
    return render(request, 'libros/mapa.html', context)