# Generated by Django 4.1.5 on 2023-01-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitaller', '0010_remove_cliente_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='precio',
            field=models.SmallIntegerField(default=0, null=0),
            preserve_default=False,
        ),
    ]
