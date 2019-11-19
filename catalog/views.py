from django.shortcuts import render
from django.utils import timezone
from .models import Pedido
from django.shortcuts import render, get_object_or_404
from .forms import PedidoForm
from django.shortcuts import redirect
    
def index(request):
    pedidos = Pedido.objects.filter(hora__lte=timezone.now()).order_by('hora')
    return render(request, 'catalog/index.html', {'pedidos': pedidos})

def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'catalog/pedido_detail.html', {'pedido': pedido})

def pedido_new(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.nombre = request.user
            pedido.sushi
            pedido.email
            pedido.direccion
            pedido.hora = timezone.now()
            pedido.save()
            return redirect('pedido_detail', pk=pedido.pk)
    else:
        form = PedidoForm()
    return render(request, 'catalog/pedido_edit.html', {'form': form})

def pedido_edit(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=post)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.nombre = request.user
            pedido.hora = timezone.now()
            pedido.save()
            return redirect('pedido_detail', pk=pedido.pk)
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'catalog/pedido_edit.html', {'form': form})