from django.db import models

class Transacao(models.Model):
    TIPOS = (
        ('R', 'Receita'),
        ('D', 'Despesa'),
    )

    descricao = models.CharField(max_length=200) # Descrição da transação com no max 200 caracteres
    valor = models.DecimalField(max_digits=10, decimal_places=2) # Valor da transação com no max 10 dígitos e 2 casas decimais
    tipo = models.CharField(max_length=1, choices=TIPOS) # Tipo da transação (R para Receita, D para Despesa)
    data = models.DateTimeField(auto_now_add=True) # Data e hora da criação da transação
    
    def __str__(self):
        return self.descricao