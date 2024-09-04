from django.db import models
from django.conf import settings
from accounts.models import Profile
from .opciones import opciones_sala_All_In_One, opciones_estado, opciones_marca_all_in_one, opciones_ubicacion_all_in_one_admin, \
    opciones_marca_notebook, opciones_ubicacion_notebook, opciones_marca_mini_pc, opciones_ubicacion_mini_pc, opciones_marca_proyector, \
    opciones_ubicacion_proyector, opciones_activos, opciones_marca_azotea, opciones_estado_activo, opciones_marca_bodega_adr, opciones_edificio

# Create your models here.
# ------------------------------------------------------------------------------------------------------------


class AllInOne(models.Model):
    activo = models.CharField(max_length=100, default='All In One', blank=True, verbose_name='Activo')
    estado = models.CharField(max_length=100, default='Seleccione',
                              choices=opciones_estado, verbose_name='Estado')
    marca = models.CharField(max_length=100, default='Seleccione',
                             choices=opciones_marca_all_in_one, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    n_serie = models.CharField(
        max_length=100, verbose_name='Número Serie')
    unive = models.CharField(max_length=100, verbose_name='UNIVE')
    bdo = models.CharField(max_length=100, verbose_name='BDO')
    netbios = models.CharField(max_length=100, verbose_name='NetBios')
    ubicacion_all_in_one = models.CharField(
        max_length=100, default='Seleccione', choices=opciones_sala_All_In_One, verbose_name='Ubicación')
    all_one_creado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                       null=True, blank=True, related_name='all_in_one_created', verbose_name='Creado por')
    fecha = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.n_serie}'


class AllInOneAdmins(models.Model):
    activo = models.CharField(max_length=100, default='All In One Admin', blank=True, verbose_name='Activo')
    estado = models.CharField(max_length=100, default='Seleccione',
                              choices=opciones_estado, verbose_name='Estado')
    marca = models.CharField(max_length=100, default='Seleccione',
                             choices=opciones_marca_notebook, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    n_serie = models.CharField(max_length=100, verbose_name='Número Serie')
    unive = models.CharField(max_length=100, verbose_name='UNIVE')
    bdo = models.CharField(max_length=100, verbose_name='BDO')
    netbios = models.CharField(max_length=100, verbose_name='NetBios')
    ubicacion_all_in_one_admin = models.CharField(
        max_length=100, default='Seleccione', choices=opciones_ubicacion_all_in_one_admin, verbose_name='Ubicación')
    all_one_adm_creado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                           null=True, blank=True, related_name='all_in_one_adm_created', verbose_name='Creado por')
    fecha = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.n_serie}'
# ________________________________________________________________________________________________________________________________________________________

# Modelo Notebook
class Notebook(models.Model):
    activo = models.CharField(max_length=150, default='Notebook', blank=True, verbose_name='Activo')
    estado = models.CharField(max_length=150, default='Seleccione',
                              choices=opciones_estado, verbose_name='Estado')
    asignado_a = models.CharField(
        max_length=150, verbose_name='Asignado a')
    marca = models.CharField(max_length=150, default='Seleccione',
                             choices=opciones_marca_notebook, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    n_serie = models.CharField(max_length=150, verbose_name='Número Serie')
    unive = models.CharField(max_length=150, verbose_name='UNIVE')
    bdo = models.CharField(max_length=150, verbose_name='BDO')
    netbios = models.CharField(max_length=150, verbose_name='NetBios')
    ubicacion_notebook = models.CharField(
        max_length=150, default='Seleccione', choices=opciones_ubicacion_notebook, verbose_name='Ubicación')
    notebook_creado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                        null=True, blank=True,  related_name='notebook_created', verbose_name='Creado por')
    fecha = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.n_serie}'

# ________________________________________________________________________________________________________________________________________________________

# Modelo Mini PC


class MiniPC(models.Model):
    activo = models.CharField(max_length=100, default='Mini PC', blank=True, verbose_name='Activo')
    estado = models.CharField(max_length=100, default='Seleccione',
                              choices=opciones_estado, verbose_name='Estado')
    marca = models.CharField(max_length=100, default='Seleccione',
                             choices=opciones_marca_mini_pc, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    n_serie = models.CharField(max_length=100, verbose_name='Número Serie')
    unive = models.CharField(max_length=100, verbose_name='UNIVE')
    bdo = models.CharField(max_length=100, verbose_name='BDO')
    ubicacion_mini_pc = models.CharField(
        max_length=100, default='Seleccione', choices=opciones_ubicacion_mini_pc, verbose_name='Ubicación')
    mini_pc_creado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                       null=True, blank=True, related_name='mini_pc_created', verbose_name='Creado por')
    fecha = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.n_serie}'
# ________________________________________________________________________________________________________________________________________________________

# Modelo Proyectores


class Proyectores(models.Model):
    activo = models.CharField(max_length=100, default='Proyector', blank=True, verbose_name='Activo')
    estado = models.CharField(max_length=100, default='Seleccione',
                              choices=opciones_estado, verbose_name='Estado')
    marca = models.CharField(max_length=100, default='Seleccione',
                             choices=opciones_marca_proyector, verbose_name='Marca')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    n_serie = models.CharField(max_length=100, verbose_name='Número Serie')
    ubicacion_proyector = models.CharField(
        max_length=100, default='Seleccione', choices=opciones_edificio, verbose_name='Edificio')
    sala = models.CharField(
        max_length=100, default='Seleccione', choices=opciones_ubicacion_proyector, verbose_name='Ubicación')
    proyector_creado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                         null=True, blank=True, related_name='proyector_created', verbose_name='Creado por')
    fecha = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.n_serie}'
# ________________________________________________________________________________________________________________________________________________________

# ________________________________________________________________________________________________________________________________________________________

# Modelo Bodega ADR
class BodegaADR(models.Model):
    activo = models.CharField(max_length=100, default='Seleccione',
                              choices=opciones_activos, verbose_name='Activo')
    marca = models.CharField(max_length=100, default='Seleccione',
                             choices=opciones_marca_bodega_adr, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    n_serie = models.CharField(max_length=100, verbose_name='Número Serie')
    unive = models.CharField(max_length=100, verbose_name='UNIVE')
    bdo = models.CharField(max_length=100, verbose_name='BDO')
    netbios = models.CharField(max_length=100, verbose_name='NetBios')
    estado_activo = models.CharField(
        max_length=100, default='Seleccione', choices=opciones_estado_activo, verbose_name='Estado Activo')
    bodega_adr_creado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                          null=True, blank=True, related_name='bodega_adr_created', verbose_name='Creado por')
    fecha = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.n_serie}'

# ________________________________________________________________________________________________________________________________________________________

# Modelo Azotea
class Azotea(models.Model):
    activo = models.CharField(max_length=100, default='Seleccione',
                              choices=opciones_activos, verbose_name='Tipo Activo')
    marca = models.CharField(max_length=100, default='Seleccione',
                             choices=opciones_marca_azotea, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    n_serie = models.CharField(max_length=100, verbose_name='Número Serie')
    unive = models.CharField(max_length=100, verbose_name='UNIVE')
    bdo = models.CharField(max_length=100, verbose_name='BDO')
    estado_activo = models.CharField(
        max_length=50, default='Seleccione', choices=opciones_estado_activo, verbose_name='Estado Activo')
    azotea_creado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                      null=True, blank=True, related_name='azotea_created', verbose_name='Creado por')
    fecha = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.n_serie}'
# ________________________________________________________________________________________________________________________________________________________
# Modelo Reporte de un equipo

class Reporte(models.Model):
    entregado_por = models.CharField(
        max_length=200, default='---------------', blank=True, null=True, verbose_name='Entregado por')
    activo = models.CharField(max_length=100, verbose_name='Activo')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    n_serie = models.CharField(max_length=100, verbose_name='Número Serie')
    unive = models.CharField(max_length=100, verbose_name='UNIVE')
    bdo = models.CharField(max_length=100, verbose_name='BDO')
    netbios = models.CharField(max_length=100, verbose_name='NetBios')
    bolso = models.BooleanField(
    default=False, blank=True, null=True, verbose_name='Bolso o Mochila',
    choices=((True, 'Sí'), (False, 'No')))
    equipo = models.BooleanField(
    default=False, blank=True, null=True, verbose_name='Equipo',
    choices=((True, 'Sí'), (False, 'No')))
    cargador = models.BooleanField(
    default=False, blank=True, null=True, verbose_name='Cargador',
    choices=((True, 'Sí'), (False, 'No')))
    reporte_creado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                       null=True, blank=True, related_name='reporte_created', verbose_name='Recepcionado por')
    en_reporte = models.BooleanField(
        default=False, blank=True, null=True, verbose_name='En Reporte',
        choices=((True, 'Sí'), (False, 'No')))
    fecha_recepcion = models.DateField(
        auto_now_add=True, verbose_name='Fecha de Recepción')

    #________________________________________________________________________________________________________________________________________
    #CAMPOS QUE MANEJAN LA ENTREGA DE UN EQUIPO YA REPORTADO
    operador_entrega = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                       null=True, blank=True, related_name='operador_entrega', verbose_name='Operador que entrega')  
    recibido_por = models.CharField(
        max_length=200, default='---------------', blank=True, null=True, verbose_name='Recibido por')
    entregado = models.BooleanField(
        default=False, blank=True, null=True, verbose_name='Entregado',
        choices=((True, 'Sí'), (False, 'No')))
    fecha_entrega = models.DateField(
        null=True, blank=True, verbose_name='Fecha entrega')
    
    def __str__(self):
        return f'{self.operador_entrega}'

# ________________________________________________________________________________________________________________________________________________________

# ________________________________________________________________________________________________________________________________________________________
# Modelo Entregar Equipo Reportado de un equipo

