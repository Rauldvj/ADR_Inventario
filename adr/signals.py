from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AllInOne, AllInOneAdmins, Notebook, MiniPC, Reporte

#Receiver para la creacion de registros


#___________________________________________________________________________________________________________________________________
@receiver(post_save, sender=AllInOne)
def crear_registro_reporte_allinone(sender, instance, created, **kwargs):
    if created:
        Reporte.objects.create(
            activo=instance.activo,
            marca=instance.marca,
            modelo=instance.modelo,
            n_serie=instance.n_serie,
            unive=instance.unive,
            bdo=instance.bdo,
            netbios=instance.netbios,
        )
 
#___________________________________________________________________________________________________________________________________




#___________________________________________________________________________________________________________________________________

@receiver(post_save, sender=AllInOneAdmins)
def crear_registro_reporte_allinoneadmin(sender, instance, created, **kwargs):
    if created:
        Reporte.objects.create(
            activo=instance.activo,
            marca=instance.marca,
            modelo=instance.modelo,
            n_serie=instance.n_serie,
            unive=instance.unive,
            bdo=instance.bdo,
            netbios=instance.netbios,
        )
#___________________________________________________________________________________________________________________________________
@receiver(post_save, sender=Notebook)
def crear_registro_reporte(sender, instance, created, **kwargs):
    if created:
        Reporte.objects.create(
            activo=instance.activo,
            marca=instance.marca,
            modelo=instance.modelo,
            n_serie=instance.n_serie,
            unive=instance.unive,
            bdo=instance.bdo,
            netbios=instance.netbios,
        )

#___________________________________________________________________________________________________________________________________

@receiver(post_save, sender=MiniPC)
def crear_registro_reporte_miniPC(sender, instance, created, **kwargs):
    if created:
        Reporte.objects.create(
            activo=instance.activo,
            marca=instance.marca,
            modelo=instance.modelo,
            n_serie=instance.n_serie,
            unive=instance.unive,
            bdo=instance.bdo,

        )