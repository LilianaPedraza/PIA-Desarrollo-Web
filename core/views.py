from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse

def home(request):
    return render(request, 'core/home.html')

def contexto(request):
    return render(request, 'core/contexto.html')

def historia(request):
    return render(request, 'core/historia.html')

def index(request):
    return render(request, 'core/index.html')

def mitos(request):
    return render(request, 'core/mitos.html')

def terminos(request):
    return render(request, 'core/terminos.html')

def tutoriales(request):
    return render(request, 'core/tutoriales.html')

def exit(request):
    logout(request)
    return redirect('home')