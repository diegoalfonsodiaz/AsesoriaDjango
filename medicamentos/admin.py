from django.contrib import admin

from medicamentos.models import Proyecto, ProyectoAdmin, Asesor, AsesorAdmin

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Asesor, AsesorAdmin)
