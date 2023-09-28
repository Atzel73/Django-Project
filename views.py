from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return render(request, 'inicio.html')
def contacto(request):
    return render(request, 'contact.html')
    