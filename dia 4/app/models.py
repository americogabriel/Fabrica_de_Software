from django.db import models

class Usuarios(models.Model):
    user = models.CharField(max_length= 100)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user
    
class Endereco(models.Model):
    endereco = models.CharField(max_length= 100)
    other = models.CharField(max_length= 100)
    email = models.EmailField()
