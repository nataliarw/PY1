# Generated by Django 4.1 on 2023-06-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("autor", models.CharField(max_length=100)),
                (
                    "valoracion",
                    models.IntegerField(help_text="Valoracion entre 0 y 5000"),
                ),
            ],
        ),
    ]
