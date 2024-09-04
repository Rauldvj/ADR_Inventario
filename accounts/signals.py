#Este archivo signals.py sirve para enrutar al momento de grabar un usuario, lo envíe automáticamente a un grupo de usuarios

from django.contrib.auth.models import Group # type: ignore
from django.dispatch import receiver # type: ignore
from django.db.models.signals import post_save # type: ignore
from .models import Profile  # Importamos el modelo Profile

# Utilizamos el decorador receiver para manejar la creación de perfiles y asignar grupos

@receiver(post_save, sender=Profile)
def add_user_to_funcionarios_group(sender, instance, created, **kwargs):
    if created:
        try:
            group1 = Group.objects.get(name='Usuario')
        except Group.DoesNotExist:
            group1 = Group.objects.create(name='Usuario')
            group2 = Group.objects.create(name='ADR')
            group3 = Group.objects.create(name='Operadores ADR')
            group4 = Group.objects.create(name='Auxiliares Operadores ADR')
            group5 = Group.objects.create(name='Alumnos en Práctica')
        instance.user.groups.add(group1)







