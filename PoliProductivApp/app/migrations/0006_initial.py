# Generated by Django 5.1.6 on 2025-03-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0005_delete_cnel_oviedo_delete_iae_delete_icm_delete_iek_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cnel. Oviedo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='IAE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ICM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='IEK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='IEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='IEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='IIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='IMK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ISP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='LCA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='LCI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='LCIk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='LEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='LGH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='TSE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asignatura', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('Seccion', models.CharField(max_length=5)),
                ('Profesor', models.CharField(max_length=80)),
                ('Primer_Parcial', models.DateTimeField()),
                ('Segundo_Parcial', models.DateTimeField()),
                ('Primer_Final', models.DateTimeField()),
                ('Horario_Semanal', models.JSONField()),
            ],
        ),
    ]
