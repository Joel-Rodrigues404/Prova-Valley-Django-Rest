from django.db import models

# Create your models here.

class Disco(models.Model):
    titulo = models.CharField(max_length=100)
    nome_do_artista = models.CharField(max_length=50)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50)
    data_de_lancamento = models.DateField()
    ESTADO_DO_DISCO = (
        ('R','Regular'),
        ('M', 'Mediano'),
        ('O', 'Otimo'),
    )
    estado_do_disco = models.CharField(max_length=1, choices=ESTADO_DO_DISCO, blank=False, null=False)

    def __str__(self) -> str:
        return self.titulo