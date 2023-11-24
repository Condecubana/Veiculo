
from django.shortcuts import render, get_object_or_404, redirect
from .models import Veiculo, Motorista, Controle
from .forms import VeiculoForm, MotoristaForm, ControleForm
from django.urls import reverse


def inicio(request):
    controles = Controle.objects.all().order_by('-data_saida', '-hora_saida')
    search = request.GET.get('search')
    if search:
        controles = Controle.objects.filter(data_saida__icontains=search)
    return render(request, 'paginas/inicio.html', {'controles': controles})

def veiculos(request):
    formulario = VeiculoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('veiculos')
    return render(request, 'controle/veiculos.html', {'formulario': formulario})

def motoristas(request):
    formulario = MotoristaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
    return render(request, 'controle/motoristas.html', {'formulario':formulario})

def controle(request):
    controle = controle.objects.all()
    return render('request,controle/controle.html', {'controle': controle})

def visualizar_movimentacao(request, id):
    controle = get_object_or_404(Controle, id=id)
    return render(request, 'controle/visualizar_movimentacao.html', {'controle': controle})

def editar_movimentacao(request, id):
   controle = Controle.objects.get(id=id)
   formulario = ControleForm(request.POST or None, request.FILES or None, instance= controle)
   if formulario.is_valid():
        formulario.save()
        return redirect('veiculos')
   return render(request, 'controle/veiculos.html', {'formulario': formulario})

    

def excluir_movimentacao(request, id):
    controle = Controle.objects.get(id= id)
    controle.delete()
    return redirect(reverse('inicio'))
  