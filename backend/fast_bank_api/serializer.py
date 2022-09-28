from .models import *
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'cpf', 'password']
        

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'cep', 'road', 'house_number', 'neighborhood', 'city', 
                 'uf', 'country']
        

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'agency', 'account_number', 'verify_digit', 'money', 
                 'class_account', 'account_type']
   

class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transferencia
        fields = ['id', 'transfer_date', 'operation_type', 'value', 
                 'sending_account', 'recive_account']


class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['id', 'loan_status','loan_date', 'loan_first_installment_date', 
                 'loan_value', 'number_installment', 'number_pay_installment',
                 'fees', 'loan_value_payment', 'total_value']
    
    def calc_first_installment_date(self):
        # days = self.loan_date.day
        months = self.loan_date.month
        return months+1
    
    def calc_loan_payment(self):
        value = self.loan_value
        installment = self.number_installment
        fees_decimal = self.fees/100
        value_payment = (value/installment)*fees_decimal
        return value_payment
    
    def calc_total_loan_payment(self):
        return self.loan_value_payment*self.number_pay_installment
    
    loan_first_installment_date = serializers.SerializerMethodField(method_name='calc_first_installment_date')
    
    loan_value_payment = serializers.SerializerMethodField(method_name='calc_loan_payment')
    
    total_value = serializers.SerializerMethodField(method_name='calc_total_loan_payment')


class PGTO_EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGTO_Emprestimo
        fields = ['id', 'date_payment','loan']


class SemBeneficioSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = SemBeneficio
        fields = ['id', 'descricao']
        
        
class PlanoSaudeSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = PlanoSaude
        fields = ['id', 'installment_value', 'plan_type', 
                 'installment_date', 'pay_installment_date', 'health_plan']
    
    pay_installment_date = serializers.SerializerMethodField(method_name='verify_type_plan')

    def verify_type_plan(self):
        if self.plan_type == "M":
            months = self.installment_date.month
            return months+1
        if self.plan_type == "A":
            years = self.installment_date.year
            return years+1
    
        
class ValeRefeicaoSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = ValeRefeicao
        fields = ['id', 'value']
    
        
class ValeAlimentacaoSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = ValeAlimentacao
        fields = ['id', 'value']
        

class BeneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficio
        fields = ['id', 'nome', 'client']
    
    detail = serializers.SerializerMethodField(method_name='verify_benefit')
    
    def verify_benefit(self):
        if self.nome == "SB":
            type = SemBeneficio
            return type
        if self.nome == "PS":
            type = PlanoSaude
            return type
        if self.nome == "VR":
            type = ValeRefeicao
            return type
        if self.nome == "VA":
            type = ValeAlimentacao
            return type


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'last_name', 'first_name', 'age', 'email', 
                 'sex_choice', 'user', 'adress', 'account']


class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ['id', 'number', 'security_number', 'validate_date', 
                 'email', 'client']


class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        field = ['id', 'emission_date', 'validate_date', 'value', 
                 'status', 'card']

    