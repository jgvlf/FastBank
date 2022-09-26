from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

# Create your views here.

class ClientesViewSets(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class UsuariosViewSets(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    
class EnderecosViewSets(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    
    
class ContasViewSets(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    
    