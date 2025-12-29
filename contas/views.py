from rest_framework import viewsets
from .models import Transacao
from .serializers import TransacaoSerializer

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all() # Exibe todas as transações
    serializer_class = TransacaoSerializer # Usa o tradutor (serializer) definido para Transacao