# Generated by Django 4.1.5 on 2023-01-26 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mitaller', '0005_tarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombremecanico', models.CharField(max_length=30)),
                ('Tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mitaller.tarea')),
            ],
        ),
    ]