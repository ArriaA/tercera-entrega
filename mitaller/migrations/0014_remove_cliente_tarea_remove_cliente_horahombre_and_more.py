# Generated by Django 4.1.5 on 2023-01-27 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mitaller', '0013_alter_cliente_horahombre_alter_tarea_tiempo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Tarea',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='horahombre',
        ),
        migrations.AddField(
            model_name='cliente',
            name='Proyecto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mitaller.proyecto'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Obrero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, null='aaa')),
                ('horahombre', models.SmallIntegerField(blank=True, default=0)),
                ('Tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mitaller.tarea')),
            ],
        ),
    ]
