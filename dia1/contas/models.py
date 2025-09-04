from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_create = models.DateTimeField()

    def __str__(self):
        return self.nome

class Transaçao(models.Model):
    data = models.DateTimeField()
    descrição = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7,decimal_places= 2)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    observaçao = models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name_plural = 'Transações'
    
    def __str__(self):
        return self.descrição

