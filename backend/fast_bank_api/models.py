from django.db import models

# Create your models here.
class Usuario(models.Model):
    cpf = models.CharField(max_length = 11, unique=True)
    password = models.CharField(max_length=30)
    
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
        return str(self.road)
    
    
    class Meta:
        verbose_name_plural = "Enderecos"
        

class Conta(models.Model):
    agency = models.CharField(max_length = 5)
    account_number = models.CharField(max_length = 7, unique=True)
    verify_digit = models.CharField(max_length = 1)
    money = models.DecimalField(max_digits=9, decimal_places=2)
    BRONZE = "Bronze"
    SILVER = "Prata"
    GOLD = "Ouro"
    DIAMOND = "Diamante"
    CLASS_ACCOUNT = [
        ("B", BRONZE),
        ("S", SILVER),
        ("G", GOLD),
        ("D", DIAMOND),
    ]
    CORRENT_ACCOUNT = "Conta Corrente"
    ESSENTIAL_ACCOUNT = "Conta Essencial"
    SAVINGS_ACCOUNT = "Conta Poupança"
    ACCOUNT_TYPE = [
        ("CC", CORRENT_ACCOUNT),
        ("CE", ESSENTIAL_ACCOUNT),
        ("CP", SAVINGS_ACCOUNT),
    ]
    class_account = models.CharField(max_length = 1, choices = CLASS_ACCOUNT, default = BRONZE)
    account_type = models.CharField(max_length = 2, choices = ACCOUNT_TYPE, default = CORRENT_ACCOUNT)
    
    def __str__(self):
        return f"{self.agency} {self.account_number}-{self.verify_digit}"
    
    class Meta:
        verbose_name_plural = "Contas"
    

class Transferencia(models.Model):
    transfer_date = models.DateField()
    DEPOSIT = "Depositar"
    WITHDRAW = "Sacar"
    OPERATION_TYPE = [
        ("D", DEPOSIT),
        ("W", WITHDRAW),
    ]
    operation_type = models.CharField(max_length = 1, choices = OPERATION_TYPE, default = DEPOSIT)
    value = models.DecimalField(max_digits = 9, decimal_places = 2)
    sending_account = models.ForeignKey(
        Conta,
        on_delete=models.PROTECT,
        related_name ="conta_dinheiro_enviada"
    )
    recive_account = models.ForeignKey(
        Conta,
        on_delete=models.PROTECT,
        related_name = "conta_dinheiro_recebido"
    )
    
    def __str__(self):
        return self.operation_type
    
    class Meta:
        verbose_name_plural = "Transferencias"
    
        

class Emprestimo(models.Model):
    loan_date = models.DateField()
    loan_value = models.DecimalField(max_digits = 9, decimal_places = 2)
    number_installment = models.PositiveIntegerField()
    number_pay_installment = models.PositiveIntegerField()
    fees = models.DecimalField(max_digits=5, decimal_places=2)

    ANALYSING = "Analisando"
    ALLOW = "Aprovado"
    DENY = "Recusado"
    LOAN_STATUS = [
        ("AN", ANALYSING),
        ("A", ALLOW),
        ("R", DENY),
    ]
    loan_status = models.CharField(max_length = 2, choices = LOAN_STATUS, default = ANALYSING)

    def __str__(self):
        return self.loan_date
    class Meta:
        verbose_name_plural = "Emprestimos"
    
        

class PGTO_Emprestimo(models.Model):
    date_payment = models.DateField(null=True)
    loan = models.OneToOneField(
        Emprestimo,
        on_delete = models.PROTECT
    )
    
    def __str__(self):
        return self.date_payment
    
    class Meta:
        verbose_name_plural = "PGTOS_Emprestimos"


class SemBeneficio(models.Model):
    descricao = models.CharField(max_length= 25, default="Sem Benefícios Atribuidos")
    
    
    class Meta:
        verbose_name_plural = "SemBeneficios"
    
    def __str__(self):
        return self.descricao


class PlanoSaude(models.Model):
    installment_value = models.DecimalField(max_digits = 6, decimal_places= 2)
    ANNUAL = "Anual"
    MONTHLY = "MONTHLY"
    PLAN_TYPE = [
        ("M", MONTHLY),
        ("A", ANNUAL),
    ]
    plan_type = models.CharField(max_length = 1, choices = PLAN_TYPE, default = MONTHLY)
    installment_date = models.DateField()
    pay_installment_date = models.DateField(blank=True, null=True)
    health_plan = models.CharField(max_length=6, default="UNIMED")
    
    def __str__(self):
        return str(self.pay_installment_date)
    
    class Meta:
        verbose_name_plural = "PlanosSaude"


class ValeRefeicao(models.Model):
    value = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self):
        return str(self.value)
    
    class Meta:
        verbose_name_plural = "ValeRefeicoes"


class ValeAlimentacao(models.Model):
    value = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.value)

    class Meta:
            verbose_name_plural = "ValeAlimentacoes"
      
      
class Cliente(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length = 255, unique = True)
    MALE = "Masculino"
    FEMALE = "Feminino"
    OTHERS = "Outros"
    SEX_CHOICES = [
      ("M", MALE),
      ("F", FEMALE),
      ("O", OTHERS),
    ]
    
    sex_choice = models.CharField(max_length = 1, choices = SEX_CHOICES, default = MALE)
    
    user = models.OneToOneField(
        Usuario,
        on_delete = models.CASCADE,  
    )
    
    adress = models.ForeignKey(
        Endereco,
        on_delete = models.CASCADE
    )
    
    account = models.OneToOneField(
        Conta,
        on_delete = models.CASCADE,
    )
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
    
    class Meta:
        verbose_name_plural = "Clientes"
    
    
class Beneficio(models.Model):
    NO_BENEFIT = "Sem Benefício"
    HEALTH_PLAN = "Plano de Saúde"
    LUNCHEON_VOUCHER = "Vale Refeição"
    FOOD_VOUCHER = "Vale Alimentação"
    BENEFIT_TYPE=[
        ("SB", NO_BENEFIT),
        ("PS", HEALTH_PLAN),
        ("VR", LUNCHEON_VOUCHER),
        ("VA", FOOD_VOUCHER),
    ]
    nome = models.CharField(max_length=2, choices = BENEFIT_TYPE, default = NO_BENEFIT)
    client = models.ForeignKey(
        Cliente,
        on_delete = models.PROTECT
    )

    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Beneficios"
class Cartao(models.Model):
    number = models.CharField(max_length= 255)
    security_number = models.CharField(max_length= 255)
    validate_date = models.CharField(max_length= 5)
    client = models.OneToOneField(
        Cliente,
        on_delete = models.PROTECT
    )
    
    def __str__(self):
        return self.number
    
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
        ("AGP", WAIT_PAYMENT),
        ("ANP", ANALYSING_PAYMENT),
        ("PA", ALLOW_PAYMENT),
        ("PR", DENY_PAYMENT),
    ]
    status = models.CharField(max_length = 3, choices = STATUS_TYPE, default = WAIT_PAYMENT)
    card = models.OneToOneField(
        Cartao,
        on_delete = models.PROTECT
    )
    
    def __str__(self):
        return self.emission_date
    
    
    class Meta:
        verbose_name_plural = "Faturas"