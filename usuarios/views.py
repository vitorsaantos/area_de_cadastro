from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm


def inicio(request):
    return render(request,'pages/home.html')

def cadastro(request):
    form = CadastroForm()
    if request.method == 'GET':
        return render(request, 'pages/cadastro.html', {
            'form': form,
        })
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuário com esse username.')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return render(request, 'pages/login.html')


def login(request):

    if request.method == 'GET':
        return render(request, 'pages/login.html')

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return render(request, 'pages/home.html')
        
        else:
            return HttpResponse('Email ou Senha invalida!')
        
def mensagens(request):
    return render(request, 'pages/mensagens.html' )
        
@login_required(login_url="/client/login/")
def cliente(request):
    return HttpResponse('AREA DO CLIENTE!!!')


