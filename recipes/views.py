from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, template_name='Home.html')  

def about(request):
    return HttpResponse('<h1>Sobre</h1>')

def contato(request):
    return HttpResponse('<h1>Contato</h1>')