from rest_framework import serializers

import accounts.serializers
from .models import Area, Sento, UserSentoVisit


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['name']


class SentoSerializer(serializers.ModelSerializer):
    area = AreaSerializer(many=False)
    point_geojson = serializers.SerializerMethodField()

    class Meta:
        model = Sento
        exclude = ['point', 'created_at', 'updated_at']

    def get_point_geojson(self, object):
        point = object.point.geojson
        return point


class UserSentoVisitSerializer(serializers.ModelSerializer):
    sento = SentoSerializer()
    user = accounts.serializers.UserSerializer()

    class Meta:
        model = UserSentoVisit
        fields = '__all__'


class UserSentoVisitPostDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSentoVisit
        fields = '__all__'
