from django.shortcuts import redirect, render, get_object_or_404
from .models import CarritoItem
from productos.models import Celular
from .forms import AgregarAlCarritoForm

def ver_carrito(request):
    items = CarritoItem.objects.all()
    return render(request, 'carrito/ver_carrito.html', {'items': items})

def agregar_al_carrito(request, celular_id):
    celular = get_object_or_404(Celular, id=celular_id)
    if request.method == 'POST':
        form = AgregarAlCarritoForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            CarritoItem.objects.create(celular=celular, cantidad=cantidad)
            return redirect('ver_carrito')
    else:
        form = AgregarAlCarritoForm()
    return render(request, 'carrito/agregar_al_carrito.html', {'form': form, 'celular': celular})
