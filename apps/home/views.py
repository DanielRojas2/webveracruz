from django.shortcuts import render
from ..contacto.forms import FormularioContacto
from django.core.mail import send_mail

# Create your views here.

def inicio(request):
    return render(request, 'home/home.html')
