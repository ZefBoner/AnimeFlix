from django.shortcuts import render, get_object_or_404
from .models import Animes

# Create your views here.

def webapp(request):
    return render(request, 'webapp/index.html')



def anime_detail(request, anime_id):
    anime = get_object_or_404(Animes, id_anime=anime_id)
    return render(request, 'webapp/anime_detail.html', {'anime': anime})


def agregar_anime(request):
    if request.method == 'POST':
        id_anime = request.POST['id_anime']
        nombre_anime = request.POST['nombre_anime']
        anime = Animes(id_anime=id_anime, nombre_anime=nombre_anime)
        anime.save()
        
    # Obtener todos los animes de la base de datos
    animes = Animes.objects.all()
    
    return render(request, 'webapp/agregar_anime.html', {'animes': animes})