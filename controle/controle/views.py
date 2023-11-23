
from django.shortcuts import render, get_object_or_404, redirect
from .models import Veiculo, Motorista, Controle
from .forms import VeiculoForm, MotoristaForm, ControleForm
from django.urls import reverse


def inicio(request):
    controles = Controle.objects.all().order_by('-data_saida', '-hora_saida')
    return render(request, 'paginas/inicio.html', {'controles': controles})

def veiculos(request):
    formulario = VeiculoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('veiculos')
    return render(request, 'controle/veiculos.html', {'formulario': formulario})

def motoristas(request):
    return render(request, 'controle/motoristas.html')

def controle(request):
    controle = controle.objects.all()
    return render('request,controle/controle.html', {'controle': controle})

def visualizar_movimentacao(request, id):
    controle = get_object_or_404(Controle, id=id)
    return render(request, 'controle/visualizar_movimentacao.html', {'controle': controle})

def editar_movimentacao(request, id):
   veiculo = Veiculo.objects.get(id=id)
   formulario = VeiculoForm(request.POST or None, request.FILES or None, instance= veiculo)
   if formulario.is_valid():
        formulario.save()
        return redirect('veiculos')
   return render(request, 'controle/veiculos.html', {'formulario': formulario})

    

def excluir_movimentacao(request, id):
    veiculo = get_object_or_404(veiculo, pk= id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect(reverse('inicio'))
    return render(request, 'controle/excluir_movimentacao.html', {'controle': controle})