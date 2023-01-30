# Generated by Django 4.1.5 on 2023-01-26 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mitaller', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombremecanico', models.CharField(max_length=30)),
                ('Task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mitaller.task')),
            ],
        ),
    ]
