from rest_framework import serializers

from .models import Area, Sento


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['name']


class SentoSerializer(serializers.ModelSerializer):
    area = AreaSerializer(many=False)

    class Meta:
        model = Sento
        fields = '__all__'
