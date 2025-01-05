from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Book

def home(request):
    books = Book.objects.all()
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
        return render(request, 'home.html', {"books" : books})

def logout_user(request):
    logout(request)
    messages.success(
        request,
        "Você fez logout com sucesso"
    )
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(
                username=username,
                password=password
            )
            login(request, user)
            messages.success(
                request,
                "Você fez login com sucesso com um novo usuário"
            )
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form' : form})
    return render(request, 'register.html', {'form' : form})

def book_detail(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id = id)
        return render(request, 'book.html', {"book" : book})
    else:
        messages.error(
            request,
            "Você precisa estar autenticado"
        )
        return redirect('home')
    
def book_delete(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        book.delete()
        messages.success(
            request,
            "Livro excluído com sucesso!"
        )
        return redirect('home')
    else:
        messages.error(
            request,
            "Você precisa estar logado"
        )
        return redirect('home')