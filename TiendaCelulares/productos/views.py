from django.shortcuts import render, get_object_or_404
from .models import Celular

def lista_celulares(request):
    celulares = Celular.objects.all()
    return render(request, 'productos/lista_celulares.html', {'celulares': celulares})

def detalle_celular(request, celular_id):
    celular = get_object_or_404(Celular, id=celular_id)
    return render(request, 'productos/detalle_celular.html', {'celular': celular})
