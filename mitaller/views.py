from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Tarea, Cliente, Obrero
from .forms import CrearNuevaTarea, CrearNuevoProyecto, CrearNuevoCliente, CrearNuevoObrero
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def proyectos(request):
    # proyecto = list(Proyecto.objects.values())
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/proyectos.html', {'proyectos': proyectos})

def crear_proyecto(request):
    if request.method == 'GET':
        return render(request, 'proyectos/crear_proyecto.html', {'form': CrearNuevoProyecto()})
    else:
        Proyecto.objects.create(name=request.POST['name'])
        return redirect('proyectos')


def proyecto_detallado(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    tareas = Tarea.objects.filter(Proyecto_id=id)
    return render(request,'proyectos/detallado.html', {'proyecto': proyecto, 'tareas': tareas})




def tareas(request):
 # tarea = Tarea.objects.get(title = title)
    tareas = Tarea.objects.all()
    return render(request, 'tareas/tareas.html', {'tareas': tareas})


def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})


def obreros(request):
    obreros = Obrero.objects.all()
    return render(request, 'obreros/obreros.html', {'obreros': obreros})



def crear_tarea(request):
    if request.method == 'GET':
        return render(request, 'tareas/crear_tarea.html', {'form': CrearNuevaTarea()})
    else:
        Tarea.objects.create(title=request.POST['title'],
                             descripcion=request.POST['descripcion'],
                             Proyecto_id=1)
        return redirect('tareas')


def crear_obrero(request):
    if request.method == 'GET':
        return render(request, 'obreros/CrearNuevoObrero.html', {'form': CrearNuevoObrero()})
    else:
        Obrero.objects.create(nombre=request.POST['nombre'],
                              horahombre=request.POST['horahombre'],
                              Proyecto_id=1)
        return redirect('obreros')


def crear_cliente(request) :
    if request.method == 'GET':
        return render(request, 'clientes/CrearNuevoCliente.html', {'form': CrearNuevoCliente()})
    else:
        Cliente.objects.create(nombre=request.POST['nombre'])
        return redirect('clientes')





"""  tareas = Tarea.objects.filter(proyecto_id=id)
    return render(request, 'proyectos/detallado.html', {'proyecto': proyecto, 'tareas': tareas})
"""

def hello(request, user):
    return HttpResponse('<h2>hello %s</h2>' % user)
