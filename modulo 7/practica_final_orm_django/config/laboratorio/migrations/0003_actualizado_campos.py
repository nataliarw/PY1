# Generated by Django 4.2.4 on 2023-08-10 01:40

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_rename_f_vencimiento_producto_f_fabricacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2015, 1, 1))]),
        ),
    ]