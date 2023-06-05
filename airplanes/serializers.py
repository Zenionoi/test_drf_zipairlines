from rest_framework import serializers

from airplanes.models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"


class AirplaneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ("id", "passengers", "tank", "consumption", "minutes")
