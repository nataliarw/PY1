# Generated by Django 4.1 on 2023-07-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehiculo", "0002_alter_vehiculo_options_alter_vehiculo_categoria_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehiculo",
            name="precio",
            field=models.IntegerField(),
        ),
    ]
