from rest_framework import serializers
from .models import Hantem


class HantemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Hantem
        fields = '__all__'
