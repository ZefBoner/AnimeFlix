from .models import Animes

def animes(request):
    #return {'animes': Animes.objects.all()}
    return {'animes': Animes.all()}
