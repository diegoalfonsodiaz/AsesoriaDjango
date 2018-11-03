from django.shortcuts import render
from django.contrib import messages
from .forms import AsesorForm
from medicamentos.models import Asesor, Asesoria

# Create your views here.

def post_list(request):
    return render(request, 'medicamentos/post_list.html', {})

def asesor_nuevo(request):
    if request.method == "POST":
        formulario = AsesorForm(request.POST)
        if formulario.is_valid():
            asesor = Asesor.objects.create(nombre=formulario.cleaned_data['nombre'], facultad = formulario.cleaned_data['facultad'], anios = formulario.cleaned_data['anios'], profesion = formulario.cleaned_data['profesion'])
            for proyecto_id in request.POST.getlist('proyectos'):
                asesoria = Asesoria(proyecto_id=proyecto_id, asesor_id = asesor.id)
                asesoria.save()
            messages.add_message(request, messages.SUCCESS, 'Asesor Guardado Exitosamente')
    else:
        formulario = AsesorForm()
    return render(request, 'medicamentos/asesor_editar.html', {'formulario': formulario})