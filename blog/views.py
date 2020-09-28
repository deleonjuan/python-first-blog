from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion


def publicacion_lista(request):
    publicaciones = Publicacion.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/publicacion_lista.html', {'publicaciones':publicaciones})
