from . import views
from rest_framework_nested.routers import DefaultRouter
from django.urls import path, include

rotas = DefaultRouter()
rotas.register('clientes', views.ClientesViewSets, basename='clientes')
rotas.register('usuarios', views.UsuariosViewSets, basename='usuarios')
rotas.register('contas', views.ContasViewSets, basename='contas')
rotas.register('enderecos', views.EnderecosViewSets, basename='enderecos')

urlpatterns = rotas.urls
