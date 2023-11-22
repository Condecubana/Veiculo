from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('veiculos/', views.veiculos, name='veiculos'),
    path('motoristas/', views.motoristas, name='motoristas'),
    path('controle/visualizar_movimentacao/<int:id>', views.visualizar_movimentacao, name='visualizar_movimentacao'),
    path('controle/editar_movimentacao', views.editar_movimentacao, name='editar_movimentacao'),
    path('controle/editar_movimentacao/<int:id>', views.editar_movimentacao, name='editar_movimentacao'),
    path('controle/', views.controle, name='controle'),
    path('controle/visualizar_movimentacao', views.visualizar_movimentacao, name='visualizar_movimentacao'),
    path('excluir_movimentacao/<int:id>', views.excluir_movimentacao, name='excluir_movimentacao'),

]