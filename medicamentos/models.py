from django.db import models
from django.contrib import admin

class Proyecto(models.Model):
    nombre                  = models.CharField(max_length=30)
    fecha_aprobado          = models.DateField()
    descripcion             = models.CharField(max_length=120)
    cantidad_integrantes    = models.IntegerField()
    nombre_integrantes      = models.CharField(max_length=250)
    carreras                = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Asesor(models.Model):
    nombre                  = models.CharField(max_length=60)
    facultad                = models.CharField(max_length=60)
    anios                   = models.IntegerField()
    profesion               = models.CharField(max_length=60)
    proyectos               = models.ManyToManyField(Proyecto, through='Asesoria')

    def __str__(self):
        return self.nombre


class Asesoria(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    asesor = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

class AseroriaInLine(admin.TabularInline):
    model = Asesoria
    extra = 1


class ProyectoAdmin(admin.ModelAdmin):
    inlines = (AseroriaInLine,)


class AsesorAdmin (admin.ModelAdmin):
    inlines = (AseroriaInLine,)