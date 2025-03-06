# Generated by Django 5.1.6 on 2025-03-02 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_cnel_oviedo_delete_iae_delete_icm_delete_iek_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IAE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.IntegerField()),
                ('Departamento', models.CharField(max_length=50)),
                ('Asignatura', models.CharField(max_length=50)),
                ('Nivel', models.CharField(max_length=50)),
                ('NivelGlobal', models.IntegerField()),
                ('Carrera', models.IntegerField()),
                ('Enfasis', models.CharField(max_length=50)),
                ('Plan', models.IntegerField()),
                ('Turno', models.CharField(max_length=50)),
                ('Seccion', models.CharField(max_length=50)),
                ('Plataforma', models.CharField(max_length=50)),
                ('Titulo', models.CharField(max_length=50)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Parcial1_dia', models.CharField(max_length=50)),
                ('Parcial1_hora', models.CharField(max_length=50)),
                ('Parcial2_dia', models.CharField(max_length=50)),
                ('Parcial2_hora', models.CharField(max_length=50)),
                ('Final1_dia', models.CharField(max_length=50)),
                ('Final1_hora', models.CharField(max_length=50)),
                ('Final2_dia', models.CharField(max_length=50)),
                ('Final2_hora', models.CharField(max_length=50)),
                ('Lunes', models.CharField(max_length=50)),
                ('Marte', models.CharField(max_length=50)),
                ('Miercoles', models.CharField(max_length=50)),
                ('Jueves', models.CharField(max_length=50)),
                ('Viernes', models.CharField(max_length=50)),
                ('Sabado', models.CharField(max_length=50)),
                ('Sabado_noche', models.CharField(max_length=50)),
            ],
        ),
    ]
