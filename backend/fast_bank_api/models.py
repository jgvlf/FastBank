from django.db import models

# Create your models here.
class Usuario(models.Model):
    cpf = models.CharField(max_length = 11, unique=True)
    password = models.CharField()
    
    def __str__(self):
        return self.cpf
    
    
    class Meta:
        verbose_name_plural = "Usuarios"

            
class Endereco(models.Model):
    country = models.CharField(max_length = 255)
    uf = models.CharField(max_length = 2)
    city = models.CharField(max_length = 255)
    neighborhood = models.CharField(max_length= 255)
    road = models.CharField(max_length = 255)
    house_number = models.CharField(max_length=10)
    cep = models.CharField(max_length = 8)
    
    def __str__(self):
        return self.id
    
    
    class Meta:
        verbose_name_plural = "Enderecos"
        
        
class Conta(models.Model):
    agency = models.CharField(max_length = 255)
    account_number = models.CharField(max_length = 255)
    verify_digit = models.CharField(max_length = 1)
    money = models.DecimalField(max_digits=9, decimal_places=2)
    BRONZE = "Bronze"
    SILVER = "Prata"
    GOLD = "Ouro"
    DIAMOND = "Diamante"
    CLASS_ACCOUNT = [
        (BRONZE, "B"),
        (SILVER, "S"),
        (GOLD, "G"),
        (DIAMOND, "D"),
    ]
    CORRENT_ACCOUNT = "Conta Corrente"
    ESSENTIAL_ACCOUNT = "Conta Essencial"
    SAVINGS_ACCOUNT = "Conta Poupança"
    ACCOUNT_TYPE = [
        (CORRENT_ACCOUNT, "CC"),
        (ESSENTIAL_ACCOUNT, "CE"),
        (SAVINGS_ACCOUNT, "CP"),
    ]
    account_type = models.CharField(max_length=15, choices=ACCOUNT_TYPE, default=1)
    
    
    class Meta:
        verbose_name_plural = "Contas"

        
class Transferencia(models.Model):
    transfer_date = models.DateField()
    DEPOSIT = "Depositar"
    WITHDRAW = "Sacar"
    OPERATION_TYPE = [
        (DEPOSIT, "D"),
        (WITHDRAW, "W"),
    ]
    operation_type = models.CharField(max_length = 9, choices = OPERATION_TYPE, default = DEPOSIT)
    value = models.DecimalField(max_digits = 9, decimal_places = 2)
    sending_account = models.ForeignKey(
        Conta,
        on_delete=models.PROTECT
    )
    recive_account = models.ForeignKey(
        Conta,
        on_delete=models.PROTECT
    )
    
    class Meta:
        verbose_name_plural = "Transferencias"
        

class Emprestimo(models.Model):
    loan_date = models.DateField()
    loan_first_installment_date = models.DateField()
    loan_value = models.DecimalField(max_digits = 9, decimal_places = 2)
    number_installment = models.PositiveBigIntegerField(max_length = 3)
    number_pay_installment = models.PositiveBigIntegerField(max_length = 3)
    fees = models.DecimalField(max_digits=5, decimal_places=2)
    
    def calc_loan_payment(self):
        value = self.loan_value
        installment = self.number_installment
        fees_decimal = self.fees/100
        value_payment = (value/installment)*fees_decimal
        return value_payment

    loan_value_payment = calc_loan_payment()
    
    total_value = loan_value_payment*number_pay_installment
    
    ANALYSING = "Analisando"
    ALLOW = "Aprovado"
    DENY = "Recusado"
    LOAN_STATUS = [
        (ANALYSING, "AN"),
        (ALLOW, "A"),
        (DENY, "R"),
    ]
    loan_status = models.CharField(max_length = 10, choices = LOAN_STATUS, default = ANALYSING)
    
    
    class Meta:
        verbose_name_plural = "Emprestimos"
class PGTO_Emprestimo(models.Model):
    date_payment = models.DateField(null=True)
    loan = models.ForeignKey(
        Emprestimo,
        on_delete = models.PROTECT
    )
    
    class Meta:
        verbose_name_plural = "PGTOS_Emprestimos"
class Beneficio(models.Model):
    class Meta:
        verbose_name_plural = "Beneficios"
    
class Cliente(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    age = models.PositiveSmallIntegerField(max_length = 3)
    email = models.EmailField(max_length = 255, unique = True)
    MALE = "Masculino"
    FEMALE = "Feminino"
    OTHERS = "Outros"
    SEX_CHOICES = [
      (MALE, "F"),
      (FEMALE, "F"),
      (OTHERS, "O"),
    ]
    
    sex_choice = models.CharField(max_length=9, choices=SEX_CHOICES, default=1)
    
    user = models.ForeignKey(
        Usuario,
        on_delete = models.CASCADE  
    )
    
    address = models.ForeignKey(
        Endereco,
        on_delete = models.CASCADE
    )
    
    account = models.ForeignKey(
        Conta,
        on_delete = models.CASCADE
    )
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
    
    class Meta:
        verbose_name_plural = "Clientes"
    
class Cartao(models.Model):
    number = models.CharField(max_length= 255)
    security_number = models.CharField(max_length= 255)
    validate_date = models.CharField(max_length= 5)
    client = models.ForeignKey(
        Cliente,
        on_delete = models.PROTECT
    )
    class Meta:
        verbose_name_plural = "Cartoes"
    
    
class Fatura(models.Model):
    emission_date = models.DateTimeField()
    validate_date = models.DateTimeField()
    value = models.DecimalField(max_digits = 9, decimal_places = 2)
    WAIT_PAYMENT = "Aguardando Pagamento"
    ANALYSING_PAYMENT = "Analisando Pagamento"
    ALLOW_PAYMENT = "Pagamento Aprovado"
    DENY_PAYMENT = "Pagamento Recusado"
    STATUS_TYPE = [
        (WAIT_PAYMENT, "AGP"),
        (ANALYSING_PAYMENT, "ANP"),
        (ALLOW_PAYMENT, "PA"),
        (DENY_PAYMENT, "PR"),
    ]
    status = models.CharField(max_length = 20, choices = STATUS_TYPE, default = WAIT_PAYMENT)
    card = models.ForeignKey(
        Cartao,
        on_delete = models.PROTECT
    )
    
    class Meta:
        verbose_name_plural = "Faturas"