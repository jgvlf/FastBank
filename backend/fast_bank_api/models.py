from django.db import models

# Create your models here.
class Usuario(models.Model):
    cpf = models.CharField(max_length = 11, unique=True)
    password = models.CharField()
    
    def __str__(self):
        return self.cpf
    
    
    class Meta:
        verbose_name_plural = "Usuarios"

            
