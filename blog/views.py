from django.shortcuts import render
from django.utils import timezone
from .models import Articulo

# Create your views here.
def listar_publicaciones (request):
    publicaciones = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_publicaciones.html', {'publicaciones':publicaciones})

def post_detail(request, pk):
    post = get_object_or_404(Articulo, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
