from rest_framework import serializers

import accounts.serializers
from .models import Area, Sento, UserSentoVisit


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['name']


class SentoSerializer(serializers.ModelSerializer):
    area = AreaSerializer(many=False)

    class Meta:
        model = Sento
        fields = '__all__'


class UserSentoVisitSerializer(serializers.ModelSerializer):
    sento = SentoSerializer()
    user = accounts.serializers.UserSerializer()

    class Meta:
        model = UserSentoVisit
        fields = '__all__'
