from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicacion
from .forms import Publicacion_formulario
from django.contrib.auth.decorators import login_required

def publicacion_lista(request):
    publicaciones = Publicacion.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/publicacion_lista.html', {'publicaciones':publicaciones})


def post_detail(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'post': post})

@login_required
def publicacion_nueva(request):
    if request.method == "POST":
        form = Publicacion_formulario(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.author = request.user
            publicacion.published_date = timezone.now()
            publicacion.save()
            return redirect('post_detail', pk=publicacion.pk)
    else:
        form = Publicacion_formulario()
    
    return render(request, 'blog/publicacion_editar.html', {'form': form})

@login_required
def publicacion_editar(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = Publicacion_formulario(request.POST, instance=publicacion)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.author = request.user
            publicacion.published_date = timezone.now()
            publicacion.save()
            return redirect('post_detail', pk=publicacion.pk)
    else:
        form = Publicacion_formulario(instance=publicacion)
    return render(request, 'blog/publicacion_editar.html', {'form': form})

@login_required
def publicaciones_borrador_lista(request):
    publicaciones = Publicacion.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/publicaciones_borrador_lista.html', {'publicaciones': publicaciones})

@login_required
def publicacion_publicar(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    post.publicar()
    return redirect('post_detail', pk=pk)

@login_required
def publicacion_borrar(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    post.delete()
    return redirect('publicacion_lista')