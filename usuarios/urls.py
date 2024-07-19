from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicial'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('mensagens/', views.mensagens, name='mensagens'),
    path('cliente', views.cliente, name='cliente'),
]
