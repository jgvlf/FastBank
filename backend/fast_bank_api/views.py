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

class TransferenciaViewSets(viewsets.ModelViewSet):
    queryset = Transferencia.objects.all()
    serializer_class = TransferenciaSerializer

class EmprestimoViewSets(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class PGTO_EmprestimoViewSets(viewsets.ModelViewSet):
    queryset = PGTO_Emprestimo.objects.all()
    serializer_class = PGTO_EmprestimoSerializer

class SemBeneficioViewSets(viewsets.ModelViewSet):
    queryset = SemBeneficio.objects.all()
    serializer_class = SemBeneficioSerializer

class PlanoSaudeViewSets(viewsets.ModelViewSet):
    queryset = PlanoSaude.objects.all()
    serializer_class = PlanoSaudeSerializer

class ValeRefeicaoViewSets(viewsets.ModelViewSet):
    queryset = ValeRefeicao.objects.all()
    serializer_class = ValeRefeicaoSerializer

class ValeAlimentacaoViewSets(viewsets.ModelViewSet):
    queryset = ValeAlimentacao.objects.all()
    serializer_class = ValeAlimentacaoSerializer

class BeneficioViewSets(viewsets.ModelViewSet):
    queryset = Beneficio.objects.all()
    serializer_class = BeneficioSerializer

class CartaoViewSets(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

class FaturaViewSets(viewsets.ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer
    
    