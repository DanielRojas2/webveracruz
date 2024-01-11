from django.shortcuts import render
from .models import Personal
# Create your views here.

def vista_personal(request):

    personal = Personal.objects.all() 
    return render(request, 'personal/personal.html', {'personal':personal})
