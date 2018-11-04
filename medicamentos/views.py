from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import AsesorForm, ProyectoForm
from medicamentos.models import Asesor, Asesoria
from .models import Proyecto, Asesor
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.  Post.objects.all()
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

def proyecto_nuevo(request):
    if request.method == "POST":
        formulario = ProyectoForm(request.POST)
        if formulario.is_valid():
            Proyecto.objects.create(nombre=formulario.cleaned_data['nombre'], fecha_aprobado = formulario.cleaned_data['fecha_aprobado'], descripcion = formulario.cleaned_data['descripcion'], cantidad_integrantes = formulario.cleaned_data['cantidad_integrantes'], nombre_integrantes = formulario.cleaned_data['nombre_integrantes'], carreras = formulario.cleaned_data['carreras'])
            messages.add_message(request, messages.SUCCESS, 'proyecto Guardado Exitosamente')
            
    else:
        formulario = ProyectoForm()
    return render(request, 'medicamentos/proyecto_editar.html', {'formulario': formulario})

def proyecto_detail(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'medicamentos/proyecto_detail.html', {'proyecto': proyecto})

def asesores_detail(request, pk):
    asesor = get_object_or_404(Asesor, pk=pk)
    return render(request, 'medicamentos/asesores_detail.html', {'asesor': asesor})

def proyectos_list(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'medicamentos/proyectos_list.html', {'proyectos': proyectos})

def asesores_list(request):
    asesores = Asesor.objects.all()
    return render(request, 'medicamentos/asesores_list.html', {'asesores': asesores})




