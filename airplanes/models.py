import math

from django.db import models


class Airplane(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    passengers = models.PositiveIntegerField()

    @property
    def tank(self) -> int:
        return self.id * 200

    @property
    def consumption(self) -> float:
        return round(math.log(self.id) * 0.8 + self.passengers * 0.002, 7)

    @property
    def minutes(self) -> int:
        return int(self.tank / self.consumption)
