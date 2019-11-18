from django.db import models
from django.utils import timezone

class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    sushi = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    direccion = models.TextField()
    hora = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.hora = timezone.now()
        self.save()

    def __str__(self):
        return self.sushi