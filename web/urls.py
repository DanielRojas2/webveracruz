from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('contacto/', include('apps.contacto.urls')),
    path('personal/', include('apps.personal.urls')),
]
