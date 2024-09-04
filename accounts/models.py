from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

#PERFIL DE USUARIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='default.png', upload_to='users/', verbose_name='Imagen de perfil')
    create_by_adr = models.BooleanField(default=True, blank=True, null=True, verbose_name='Creado por ADR')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']
    
    
    def __str__(self):
        return self.user.username
    
#AL momento de crear el usuario se creara también el perfil

def create_user_profile(sender, instance, created, **kwargs): #Función para crear el perfil de usuario
    if created:
        Profile.objects.create(user=instance)

#Funcion cuando se grabe el perfil se guarde en la BD de perfil
def save_user_profile(sender, instance, **kwargs): #Función para guardar el perfil de usuario
    instance.profile.save()

post_save.connect(create_user_profile, sender=User) #Conectar la función
post_save.connect(save_user_profile, sender=User) #Conectar la función