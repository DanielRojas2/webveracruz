from django.urls  import path
from apps.personal import views

urlpatterns = [
    path('', views.vista_personal, name = 'personal'),
]