from django.contrib import admin
from .models import Proyecto, Tarea, Cliente, Obrero

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Cliente)
admin.site.register(Obrero)


