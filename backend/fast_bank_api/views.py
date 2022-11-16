import decimal
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
    def create(self, request, *args, **kwargs):
        conta_1 = Conta.objects.get(id=self.request.data["sending_account"])
        conta_2 = Conta.objects.get(id=self.request.data["recive_account"])
        print(conta_1)
        print(conta_2)
        conta_1.money -= decimal.Decimal(self.request.data["value"])
        conta_2.money += decimal.Decimal(self.request.data["value"])
        conta_1_atualizar = {"agency": conta_1.agency, 
                                "account_number": conta_1.account_number, 
                                "verify_digit": conta_1.verify_digit,
                                "money":conta_1.money,
                                "class_account": conta_1.class_account,
                                "account_type": conta_1.account_type,
                                }
        conta_2_atualizar = {"agency": conta_2.agency, 
                                "account_number": conta_2.account_number, 
                                "verify_digit": conta_2.verify_digit,
                                "money":conta_2.money,
                                "class_account": conta_2.class_account,
                                "account_type": conta_2.account_type,
                                }
        serializer_1 = ContaSerializer(conta_1, data=conta_1_atualizar)
        if serializer_1.is_valid():
            serializer_1.save()
        else:
            print(serializer_1.errors)
        serializer_2 = ContaSerializer(conta_2, data=conta_2_atualizar)
        if serializer_2.is_valid():
            serializer_2.save()
        else:
            print(serializer_2.errors)           
            
        return super().create(request, *args, **kwargs)

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
    
    