from django.contrib import admin

from apps.personal.models import Personal

# Register your models here.

class PersonalAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')

admin.site.register(Personal, PersonalAdmin)