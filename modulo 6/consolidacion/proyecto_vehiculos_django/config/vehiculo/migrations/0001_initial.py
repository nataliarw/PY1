# Generated by Django 4.2.3 on 2023-07-10 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(default='Ford', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.IntegerField(max_length=50)),
                ('serial_motor', models.IntegerField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
                'permissions': [('development', 'Permiso como Desarrollador'), ('scrum_master', 'Permiso como scrum_master'), ('Product_owner', 'Permiso como Product_Owner')],
            },
        ),
    ]