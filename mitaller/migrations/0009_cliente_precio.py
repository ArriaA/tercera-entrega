# Generated by Django 4.1.5 on 2023-01-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitaller', '0008_remove_cliente_nombremecanico'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='precio',
            field=models.CharField(max_length=30, null='aaa'),
            preserve_default='aaa',
        ),
    ]
