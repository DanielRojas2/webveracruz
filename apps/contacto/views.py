from django.shortcuts import render
from apps.contacto.forms import FormularioContacto
from django.core.mail import send_mail

# Create your views here.

def contacto(request):
    miFormulario=FormularioContacto()
    if request.method == "POST":
        miFormulario = FormularioContacto(request.POST)

        if miFormulario.is_valid():
            asunto = 'Mensaje desde la página web'
            nombre = miFormulario.cleaned_data['nombre']
            email = miFormulario.cleaned_data['email']
            to = 'danielrojas.alvaro2@gmail.com'
            mensaje = miFormulario.cleaned_data['mensaje']
            mensaje_completo = f'El usuario {nombre}, le manda el siguiente mensaje: \n{mensaje}. \nEste es su correo si desea responder: {email}'

            send_mail(asunto, mensaje_completo, email, [to])
            miFormulario=FormularioContacto()
            
    return render(request, 'contacto/contacto.html', {"form":miFormulario})
