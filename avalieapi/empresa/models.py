from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Entidade(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Define a classe como abstrata

    def __str__(self):
        return super().__str__()

class Empresa(Entidade):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return self.nome

class Pergunta(Entidade):
    descricao = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Avaliacao(Entidade):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    comentario = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resposta