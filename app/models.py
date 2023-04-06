from django.db import models
from django.contrib.auth.models import User

class GymModel(models.Model):
    tituloejercicio = models.CharField(max_length=30)
    descripcion = models.TextField()
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name=  "publisher")
    image = models.ImageField(upload_to="posts", null= True, blank= True) 

    @property
    def image_url(self):
        return self.image.url if self.image else ''
    
    def __str__(self):
        return f"{self.tituloejercicio} - {self.descripcion} "
    
class Profile(models.Model):
    user = models.OneToOneField(to = User, on_delete=models.CASCADE, related_name= "profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''
    

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")