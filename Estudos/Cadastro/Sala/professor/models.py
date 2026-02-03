from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome