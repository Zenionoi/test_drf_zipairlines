from rest_framework import serializers

from airplanes.models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"


class AirplaneListSerializer(AirplaneSerializer):
    pass


class AirplaneDetailSerializer(AirplaneSerializer):
    class Meta:
        model = Airplane
        fields = ("id", "passengers", "tank", "consumption", "minutes")
