from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Introduce tu nombre', max_length=100)
    email = forms.EmailField(label='Introduce tu correo electrónico')
    mensaje = forms.CharField(label='Introduce tu mensaje', widget=forms.Textarea)

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not nombre:
            raise forms.ValidationError("El campo de nombre no puede estar vacío.")
        return nombre

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError("El campo de email no puede estar vacío.")
        return email

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        if not mensaje:
            raise forms.ValidationError("El campo de mensaje no puede estar vacío.")
        return mensaje