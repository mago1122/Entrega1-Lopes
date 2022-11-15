# Generated by Django 4.1.2 on 2022-11-15 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('año_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Miembros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
            ],
        ),
    ]
