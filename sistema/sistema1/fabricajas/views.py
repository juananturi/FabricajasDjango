from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return render(request, 'paginas/index.html')


def nosotros(request):
    return render(request, 'paginas/about.html')


def certificado(request):
    return render(request, 'cajas/certificados.html')


def precio(request):
    return render(request, 'cajas/price.html')


def exhibition(request):
    return render(request, 'cajas/project.html')


def service(request):
    return render(request, 'cajas/service.html')


def segunda(request):
    return render(request, 'cajas/segunda.html')
