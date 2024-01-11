from django.urls  import path
from apps.contacto import views

urlpatterns = [
    path('', views.contacto, name = 'contacto'),
]
