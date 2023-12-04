# Generated by Django 4.2.6 on 2023-12-04 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReservaAula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('nombre_reservante', models.CharField(max_length=100)),
                ('email_reservante', models.EmailField(max_length=254)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appreserva.aula')),
            ],
        ),
    ]