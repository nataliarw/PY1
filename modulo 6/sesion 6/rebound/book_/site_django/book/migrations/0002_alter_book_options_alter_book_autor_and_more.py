# Generated by Django 4.1 on 2023-07-06 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "permissions": [
                    ("development", "Permiso como Desarrollador"),
                    ("scrum_master", "Permiso como scrum_master"),
                    ("Product_owner", "Permiso como Product_Owner"),
                ]
            },
        ),
        migrations.AlterField(
            model_name="book",
            name="autor",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="book",
            name="titulo",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="book",
            name="valoracion",
            field=models.IntegerField(help_text="Valoracion entre 0 y 10000"),
        ),
    ]
