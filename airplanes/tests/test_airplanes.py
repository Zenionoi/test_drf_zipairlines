from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from airplanes.models import Airplane
from airplanes.serializers import AirplaneSerializer, AirplaneDetailSerializer

AIRPLANE_URL = reverse("airplanes:airplane-list")


def sample_airplane(**params):
    defaults = {
        "id": 9,
        "passengers": 90,
    }
    defaults.update(params)

    return Airplane.objects.create(**defaults)


class AirplaneTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.airplane = sample_airplane()

    def test_list(self):

        res = self.client.get(AIRPLANE_URL)

        serializer = AirplaneSerializer(
            Airplane.objects.all(), many=True
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_airplane(self):
        res = self.client.get(AIRPLANE_URL + f"{self.airplane.id}/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, AirplaneDetailSerializer(self.airplane).data)

    def test_deny_similar_id(self):
        res = self.client.post(AIRPLANE_URL, {"id": "9", "passengers": "90"}, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
