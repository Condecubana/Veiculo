
from django.db import models

class Veiculo(models.Model):
    placa = models.CharField(max_length=20)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    km_troca_oleo = models.IntegerField()

    def __str__(self):
        return f"{self.placa} - {self.marca}"  

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cnh= models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Controle(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    data_saida = models.DateField()
    hora_saida = models.TimeField()
    km_saida = models.IntegerField()
    destino = models.CharField(max_length=255)
    data_retorno = models.DateField(null=True, blank=True)
    hora_retorno = models.TimeField(null=True, blank=True)
    km_retorno = models.IntegerField(null=True, blank=True)
    km_percorrido = models.IntegerField(null=True, blank=True) 
     
    def __str__(self):
        return f"{self.veiculo} - {self.motorista}"