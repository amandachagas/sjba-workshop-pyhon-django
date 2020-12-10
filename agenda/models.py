from django.db import models

# Create your models here.

class Contato(models.Model):
	nome = models.CharField(max_length=300)
	telefone = models.CharField(max_length=300)
