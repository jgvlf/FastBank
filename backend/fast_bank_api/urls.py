from . import views
from rest_framework_nested.routers import DefaultRouter
from django.urls import path, include

rotas = DefaultRouter()
rotas.register('clientes', views.ClientesViewSets, basename='clientes')
urlpatterns = rotas.urls
