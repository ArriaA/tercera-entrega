# Generated by Django 4.1.5 on 2023-01-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitaller', '0006_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=30, null='aaa'),
            preserve_default='aaa',
        ),
    ]