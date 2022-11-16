from . import views
from rest_framework_nested.routers import DefaultRouter
from django.urls import path, include

rotas = DefaultRouter()
rotas.register('clientes', views.ClientesViewSets, basename='clientes')
rotas.register('usuarios', views.UsuariosViewSets, basename='usuarios')
rotas.register('contas', views.ContasViewSets, basename='contas')
rotas.register('enderecos', views.EnderecosViewSets, basename='enderecos')
rotas.register('transferencias', views.TransferenciaViewSets, basename='transferencias')
rotas.register('emprestimos', views.EmprestimoViewSets, basename='emprestimos')
rotas.register('pgto_emprestimos', views.PGTO_EmprestimoViewSets, basename='pgto_emprestimos')
rotas.register('sem_beneficios', views.SemBeneficioViewSets, basename='sem_beneficios')
rotas.register('planos_saude', views.PlanoSaudeViewSets, basename='planos_saude')
rotas.register('vales_refeicao', views.ValeRefeicaoViewSets, basename='vales_refeicao')
rotas.register('vales_alimentacao', views.ValeAlimentacaoViewSets, basename='vales_alimentcao')
rotas.register('beneficios', views.BeneficioViewSets, basename='beneficios')
rotas.register('cartoes', views.CartaoViewSets, basename='cartoes')
rotas.register('fatura', views.FaturaViewSets, basename='fatura')

urlpatterns = rotas.urls
