# Generated by Django 5.1.7 on 2025-03-23 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('data_hora', models.DateTimeField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoProblema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('arquivo', models.FileField(upload_to='anexos/')),
                ('denuncia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFormularioDeDenuncias.denuncia')),
            ],
        ),
        migrations.AddField(
            model_name='denuncia',
            name='tipo_problema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppFormularioDeDenuncias.tipoproblema'),
        ),
    ]
