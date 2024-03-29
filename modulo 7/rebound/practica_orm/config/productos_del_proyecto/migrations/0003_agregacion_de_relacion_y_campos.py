# Generated by Django 4.2.3 on 2023-07-27 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos_del_proyecto', '0002_alter_producto_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('pais', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='f_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=60),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
        migrations.AddField(
            model_name='producto',
            name='fabrica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos_del_proyecto.fabrica'),
        ),
    ]
