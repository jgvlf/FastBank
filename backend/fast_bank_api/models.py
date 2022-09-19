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
