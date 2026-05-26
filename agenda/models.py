from django.db import models

# Create your models here.
#ORM --> Object-Relational Mapper

#Contato
    #nome
    #telefone
    #endereco
    #email
    #data_nascimento

class Contato(models.Model):
    #Criando o campo nome, com max de 255 caracteres, preenchimento obrigatorio
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.nome} [{self.email}]'