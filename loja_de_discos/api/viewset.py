from rest_framework import viewsets
from loja_de_discos.api.serializer import DiscoSerializer
from loja_de_discos.models import Disco

class DiscoViewSet(viewsets.ModelViewSet):
    queryset = Disco.objects.all()
    serializer_class = DiscoSerializer

