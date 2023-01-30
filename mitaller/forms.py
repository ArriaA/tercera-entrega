from django import forms


class CrearNuevaTarea(forms.Form):
    title = forms.CharField(label='titulo de la tarea', max_length=30)
    descripcion = forms.CharField(widget=forms.Textarea)


class CrearNuevoProyecto(forms.Form):
    name = forms.CharField(label='Nombre del Proyecto',  max_length=30)

class CrearNuevoCliente(forms.Form):
    nombre = forms.CharField(label='Nombre del CLiente',  max_length=30)

class CrearNuevoObrero(forms.Form):
    nombre = forms.CharField(label='Nombre del Obrero',  max_length=30)
    horahombre = forms.IntegerField() #label='Hora Hombre') 

   
