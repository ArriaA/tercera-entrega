
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:user>', views.hello, name='hello'),
   
    path('proyectos/', views.proyectos, name='proyectos'),

   path('proyectos/<int:id>', views.proyecto_detallado,
                                        name='proyecto_detallado'),

    path('crear_proyecto/', views.crear_proyecto,    name='crear_proyecto'),
   
    
    path('tareas/', views.tareas, name='tareas'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),

    path('clientes/', views.clientes, name='clientes'),
    
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
   
    path('crear_obrero/', views.crear_obrero, name='crear_obrero'),
    path('obreros/', views.obreros, name='obreros'),
   
]
