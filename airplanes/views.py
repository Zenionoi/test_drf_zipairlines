from rest_framework import viewsets

from airplanes.models import Airplane

from airplanes.serializers import (AirplaneSerializer,
                                   AirplaneListSerializer,
                                   AirplaneDetailSerializer)


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return AirplaneListSerializer

        if self.action == "retrieve":
            return AirplaneDetailSerializer

        return self.serializer_class
