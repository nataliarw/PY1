# Generated by Django 4.2.4 on 2023-08-05 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='f_vencimiento',
            new_name='f_fabricacion',
        ),
    ]