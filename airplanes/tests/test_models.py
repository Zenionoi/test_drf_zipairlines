import pytest
from airplanes.models import Airplane
from django.db.utils import IntegrityError


@pytest.mark.django_db
def test_airplane_creation():
    airplane = Airplane.objects.create(id=12, passengers=120)

    assert airplane.id == 12 and airplane.passengers == 120


@pytest.mark.django_db
def test_id_negative():
    with pytest.raises(IntegrityError):
        Airplane.objects.create(id=-10, passengers=120)


@pytest.mark.django_db
def test_passengers_negative():
    with pytest.raises(IntegrityError):
        Airplane.objects.create(id=10, passengers=-120)


@pytest.fixture
def airplane():
    return Airplane.objects.create(id=12, passengers=120)


@pytest.mark.django_db
def test_tank_calculation(airplane):
    assert airplane.tank == 2400


@pytest.mark.django_db
def test_consumption_calculation(airplane):
    assert airplane.consumption == 2.2279253


@pytest.mark.django_db
def test_minutes_calculation(airplane):
    assert airplane.minutes == 1077
