from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, template_name='Home.html', status='201')  

def about(request):
    return render(request, template_name='sobre.html')

def contato(request):
    return render(request, template_name='contato.html')