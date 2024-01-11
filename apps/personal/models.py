from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Personal(models.Model):

    nombre_personal = models.CharField(max_length = 70, blank = False, null = False)
    foto_personal = models.ImageField(upload_to='personal')
    enlace_contacto_1 = models.URLField(max_length=255, blank = False, null = False)
    enlace_contacto_2 = models.URLField(max_length=255, blank = True, null = True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='personal'
        verbose_name_plural='personales'

    def __str__(self):
        return f'Nombre: {self.nombre_personal}'
