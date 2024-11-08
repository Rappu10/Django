from django.db import models
from productos.models import Celular

class CarritoItem(models.Model):
    celular = models.ForeignKey(Celular, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.celular.nombre}"
