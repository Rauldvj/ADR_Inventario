from django.contrib import admin
from .models import AllInOne, AllInOneAdmins, Notebook, MiniPC, Proyectores, Azotea, BodegaADR, Reporte

# Register your models here.

#All In One
class AllInOneAdmin(admin.ModelAdmin):
    list_display = ('activo','estado', 'marca', 'modelo', 'n_serie', 'unive', 'bdo', 'netbios', 'ubicacion_all_in_one', 'all_one_creado', 'fecha')

admin.site.register(AllInOne, AllInOneAdmin)
#---------------------------------------------------------------------------------------------------------------------------------

#All In One Admin
class AllInOneAdmin_Admin(admin.ModelAdmin):
    list_display = ('activo', 'estado', 'marca', 'modelo', 'n_serie', 'unive', 'bdo', 'netbios', 'ubicacion_all_in_one_admin', 'all_one_adm_creado', 'fecha')

admin.site.register(AllInOneAdmins, AllInOneAdmin_Admin)
#---------------------------------------------------------------------------------------------------------------------------------

#Notebook Admin

class NotebookAdmin(admin.ModelAdmin):
    list_display = ('activo', 'estado', 'asignado_a', 'marca', 'modelo', 'n_serie', 'unive', 'bdo', 'netbios', 'ubicacion_notebook', 'notebook_creado', 'fecha') 

admin.site.register(Notebook, NotebookAdmin)

#---------------------------------------------------------------------------------------------------------------------------------

#Mini PC Admin

class MiniPCAdmin(admin.ModelAdmin):
    list_display = ('activo', 'estado', 'marca', 'modelo', 'n_serie', 'unive', 'bdo', 'ubicacion_mini_pc', 'mini_pc_creado', 'fecha') 

admin.site.register(MiniPC, MiniPCAdmin)

#---------------------------------------------------------------------------------------------------------------------------------
#Proyectores Admin

class ProyectoresAdmin(admin.ModelAdmin):
    list_display = ('activo', 'estado', 'marca', 'modelo', 'n_serie', 'ubicacion_proyector', 'sala', 'proyector_creado', 'fecha')

admin.site.register(Proyectores, ProyectoresAdmin)
#---------------------------------------------------------------------------------------------------------------------------------

#Azotea Admin

class AzoteaAdmin(admin.ModelAdmin):
    list_display = ('activo', 'marca', 'modelo', 'n_serie', 'unive', 'bdo', 'estado_activo', 'azotea_creado', 'fecha')

admin.site.register(Azotea, AzoteaAdmin)

#---------------------------------------------------------------------------------------------------------------------------------

#BodegaADRAdmin

class BodegaADRAdmin(admin.ModelAdmin):
    list_display = ('activo', 'marca', 'modelo', 'n_serie', 'unive', 'bdo', 'netbios', 'estado_activo', 'bodega_adr_creado', 'fecha' )

admin.site.register(BodegaADR, BodegaADRAdmin)

#---------------------------------------------------------------------------------------------------------------------------------

#Reporte

class ReporteAdmin(admin.ModelAdmin):
    list_display = ('entregado_por','activo', 'marca', 'modelo', 'n_serie',\
                    'unive', 'bdo', 'netbios', 'bolso', 'equipo', 'cargador',\
                    'reporte_creado', 'en_reporte', 'fecha_recepcion', 'operador_entrega','recibido_por', 'entregado', 'fecha_entrega')
    
admin.site.register(Reporte, ReporteAdmin)      

#---------------------------------------------------------------------------------------------------------------------------------

