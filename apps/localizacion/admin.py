from django.contrib import admin
from apps.localizacion.models import *
# Register your models here.
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(Barrio)
admin.site.register(Calle)
