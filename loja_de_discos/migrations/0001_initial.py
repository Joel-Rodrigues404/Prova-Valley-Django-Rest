# Generated by Django 4.1 on 2022-09-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('nome_do_artista', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(max_length=50)),
                ('data_de_lancamento', models.DateField()),
                ('estado_do_disco', models.CharField(choices=[('R', 'Regular'), ('M', 'Mediano'), ('O', 'Otimo')], max_length=1)),
            ],
        ),
    ]
