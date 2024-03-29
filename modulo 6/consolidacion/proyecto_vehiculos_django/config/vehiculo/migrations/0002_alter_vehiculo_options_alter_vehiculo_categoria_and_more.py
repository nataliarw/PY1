# Generated by Django 4.2.3 on 2023-07-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar', 'Permiso para visualizar')], 'verbose_name': 'Vehiculo', 'verbose_name_plural': 'Vehiculos'},
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(choices=[('Particular', 'PARTICULAR'), ('Carga', 'CARGA'), ('Trasporte', 'TRANSPORTE')], default='Particular', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(choices=[('Ford', 'FORD'), ('Fiat', 'FIAT'), ('Toyota', 'TOYOTA'), ('Chevrolet', 'CHEVROLET')], default='Ford', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='serial_carroceria',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='serial_motor',
            field=models.IntegerField(),
        ),
    ]
