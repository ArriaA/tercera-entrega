from django.db import models

# Create your models here.

"""
class Project(models.Model):
    name = models.CharField(max_length=30)


class Task(models.Model):
    title = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=30)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Mecanico(models.Model):
    nombremecanico = models.CharField(max_length=30)
    horahombre = models.IntegerField
    Task = models.ForeignKey(Task, on_delete=models.CASCADE)

"""
class Proyecto(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tarea(models.Model):
    title = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=30)
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    tiempo = models.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return self.title + '-' + self.Proyecto.name


class Cliente(models.Model):
    nombre = models.CharField(max_length=30, null='aaa')
  #  Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 


class Obrero(models.Model):
    nombre = models.CharField(max_length=30, null='aaa')
    horahombre = models.SmallIntegerField(blank=True, default=0)
 #   Tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 