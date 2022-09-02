from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def login(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                #login(request, user)
                return HttpResponse(request, '/store')
            else:
                #return HttpResponse(request, '/store')
                return redirect('store')

    credenciais = LoginForm()
    context = {
        'form':credenciais,
    }
    return render(request, 'store/login.html', context)