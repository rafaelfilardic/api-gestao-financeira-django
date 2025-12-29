from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contas.views import TransacaoViewSet

# Cria rotas automaticamente para o ViewSet
routers = DefaultRouter()
routers.register(r'transacoes', TransacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls)), # Todos os endereços da API estarão sob /api/
]