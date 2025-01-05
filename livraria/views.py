from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        senha = request.POST['senha']
        
        user = authenticate(
            request, 
            username=username, 
            password=senha
        )
        
        if user is not None:
            login(request, user)
            messages.success(
                request,
                "Login realizado com sucesso"
            )
            return redirect('home')
        else:
            messages.error(
                request,
                "Erro na autenticação. Tente novamente!"
            )
            return redirect('home')
    else:
        return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.success(
        request,
        "Você fez logout com sucesso"
    )
    return redirect('home')

def register(request):
    return render(request, 'register.html')