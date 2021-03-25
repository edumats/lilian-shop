from rest_framework import serializers
from .models import Hantem


class HantemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hantem
        fields = '__all__'
        lookup_field = 'slug'
