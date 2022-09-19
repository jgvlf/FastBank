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
        

class Emprestimo(models.Model):
    class Meta:
        verbose_name_plural = "Emprestimos"
class PGTO_Emprestimo(models.Model):
    class Meta:
        verbose_name_plural = "PGTOS_Emprestimos"
class Beneficio(models.Model):
    class Meta:
        verbose_name_plural = "Beneficios"
    
