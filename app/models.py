from django.db import models


class GymModel(models.Model):
    tituloejercicio = models.CharField(max_length=30)
    descripcion = models.TextField()
    def __str__(self):
        return f"{self.tituloejercicio} - {self.descripcion}"
    
