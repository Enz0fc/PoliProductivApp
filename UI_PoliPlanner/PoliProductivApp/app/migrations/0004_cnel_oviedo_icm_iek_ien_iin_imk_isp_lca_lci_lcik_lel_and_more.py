# Generated by Django 5.1.6 on 2025-03-02 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cnel_Oviedo',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='ICM',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='IEK',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='IEN',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='IIN',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='IMK',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='ISP',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='LCA',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='LCI',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='LCIk',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='LEL',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='LGH',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.CreateModel(
            name='TSE',
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
                ('Email', models.EmailField(max_length=50)),
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
        migrations.AlterField(
            model_name='iae',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]
