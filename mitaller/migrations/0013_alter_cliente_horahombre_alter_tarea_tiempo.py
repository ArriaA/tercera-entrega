# Generated by Django 4.1.5 on 2023-01-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitaller', '0012_remove_cliente_precio_cliente_horahombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='horahombre',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='tiempo',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
    ]
