from .models import Animes

def animes(request):
    return {'animes': Animes.objects.all()}
