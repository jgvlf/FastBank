from . import views
from rest_framework_nested.routers import DefaultRouter
from django.urls import path, include

rotas = DefaultRouter()
rotas.register('clientes', )
urlpatterns = rotas.urls
