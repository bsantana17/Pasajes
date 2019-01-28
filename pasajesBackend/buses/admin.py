from django.contrib import admin

from .models import Bus, Asiento, Trayecto, Horario

admin.site.register(Bus)
admin.site.register(Asiento)
admin.site.register(Trayecto)
admin.site.register(Horario)