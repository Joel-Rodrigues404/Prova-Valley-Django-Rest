from rest_framework import serializers
from loja_de_discos.models import Disco


class DiscoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disco
        fields = '__all__'