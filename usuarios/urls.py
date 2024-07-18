from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('inicio/', views.inicio, name='inicial'),
    path('cliente', views.cliente, name='cliente'),
]
