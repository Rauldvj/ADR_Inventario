from django.urls import path # type: ignore
from django.contrib.auth.views import LogoutView # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth import views as auth_views # type: ignore
from .views import LoginView, IndexView, ProfileListView, ProfileUpdateView, HomeView, CustomLoginView, ProfilePasswordChangeView, \
    AllInOneView, Add_AllInOneView,  \
    AllInOneAdminView, NotebooksView, MiniPCView, ProyectoresView, BodegaADRView, AzoteaView, \
    ErrorView, DescargarExcelView, \
    Add_AllInOneAdminView, AddNotebooksView, AddMiniPCView, AddProyectorView, AddBodegaADRView, AddAzoteaView, AddUserView, \
    ReporteView, AddReporteView, ReporteEquipoDetailView, \
    Edit_AllInOneView, Edit_AllInOneAdmView, EditReporteEquipoView, EntregaEquiposView, EditEntregaEquipoView, \
    Edit_NotebooksView, Edit_MiniPCView, Edit_ProyectorView, Edit_BodegaADRView, Edit_AzoteaView
   
urlpatterns = [

    #URL LOGIN (PAGINA DE LOGIN)
    

    path('', CustomLoginView.as_view(), name='login'),

    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    #URL PARA AGREGAR UN USUARIO
    path(
    'add_user/', login_required(AddUserView.as_view()), name="add_user"),
    # #URL INDEX (PAGINA PRINCIPAL)
    # path('', IndexView.as_view(), name="index"), 

    #URL DE CAMBIO DE CONTRASEÑA
    path('password_change/', login_required(ProfilePasswordChangeView.as_view()), name="profile_password_change"),

    #URL PARA EDITAR UN PERFIL DE USUARIO
    path('profile_edit/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_update'),

    #URL PARA LISTAR LOS USUARIOS
    path('profile_list/', login_required(ProfileListView.as_view()), name="profile_list"), 
    
    #URL HOME (PAGINA PRINCIPAL)
    path('home/', login_required(HomeView.as_view()), name="home"),

    #URL ERROR (PAGINA DE ERROR)
    path('error/', ErrorView.as_view(), name="error"),

    #URL PARA EXPORTAR A EXCEL
    path('descargar/excel/<str:model_name>/', login_required(DescargarExcelView.as_view()), name="descargar_excel"),



    #URL ADD_ALL_IN_ONE (PAGINA PARA AGREGAR UN REGISTRO)
    path('add_all_in_one/', login_required(Add_AllInOneView.as_view()), name="add_all_in_one"),

    #URL EDIT_ALL_IN_ONE (PAGINA PARA EDITAR UN REGISTRO)
    path('edit_all_in_one/<int:pk>/', login_required(Edit_AllInOneView.as_view()), name="edit_all_in_one"),
    
    #URL ALL_IN_ONE (PAGINA CON TODOS LOS REGISTROS)
    path('all_in_one/', login_required(AllInOneView.as_view()), name="all_in_one"),
    
    #URL ADD_ALL_IN_ONE_ADMIN (PAGINA PARA AGREGAR UN REGISTRO DE ALL IN ONE ADMINISTRADORES)
    path('add_all_in_one_admin/', login_required(Add_AllInOneAdminView.as_view()), name="add_all_in_one_admin"),

    #URL ALL_IN_ONE_ADMIN (PAGINA CON TODOS LOS REGISTROS)
    path('all_in_one_adm/', login_required(AllInOneAdminView.as_view()), name="all_in_one_adm"),

    #URL EDIT_ALL_IN_ONE_ADMIN (PAGINA PARA EDITAR UN REGISTRO DE ALL IN ONE ADMINISTRADORES)
    path('edit_all_in_one_adm/<int:pk>/', login_required(Edit_AllInOneAdmView.as_view()), name="edit_all_in_one_adm"),

    #URL ADD_NOTEBOOKS (PAGINA PARA AGREGAR UN REGISTRO DE NOTEBOOKS)
    path('add_notebook/', login_required(AddNotebooksView.as_view()), name="add_notebook"),

    #URL EDIT_NOTEBOOKS (PAGINA PARA EDITAR UN REGISTRO DE NOTEBOOKS)
    path('edit_notebook/<int:pk>/', login_required(Edit_NotebooksView.as_view()), name="edit_notebook"),

    #URL NOTEBOOKS (PAGINA CON TODOS LOS REGISTROS DE NOTEBOOKS)
    path('notebooks/', login_required(NotebooksView.as_view()), name="notebooks"),

    #URL ADD_MINI_PC (PAGINA PARA AGREGAR UN REGISTRO DE MINI PC)
    path('add_mini_pc/', login_required(AddMiniPCView.as_view()), name="add_mini_pc"),

    #URL EDIT_MINI_PC (PAGINA PARA EDITAR UN REGISTRO DE MINI PC)
    path('edit_mini_pc/<int:pk>/', login_required(Edit_MiniPCView.as_view()), name="edit_mini_pc"),

    #URL MINI_PC (PAGINA CON TODOS LOS REGISTROS DE MINI PC)
    path('mini_pc/', login_required(MiniPCView.as_view()), name="mini_pc"),

    #URL PARA AGREGAR UN PROYECTOR
    path('add_proyector/', login_required(AddProyectorView.as_view()), name= 'add_proyector'),

    #URL EDIT_PROYECTOR (PAGINA PARA EDITAR UN REGISTRO DE PROYECTORES)
    path('edit_proyector/<int:pk>/', login_required(Edit_ProyectorView.as_view()), name="edit_proyector"),

    #URL PROYECTORES (PAGINA CON TODOS LOS REGISTROS DE PROYECTORES)
    path('proyectores/', login_required(ProyectoresView.as_view()), name="proyectores"),

    #URL PARA AGREGAR UN ACTIVO EN BODEGA ADR
    path('add_bodega_adr/', login_required(AddBodegaADRView.as_view()), name="add_bodega_adr"),

    #URL EDIT_BODEGA_ADR (PAGINA PARA EDITAR UN REGISTRO DE BODEGA ADR)
    path('edit_bodega_adr/<int:pk>/', login_required(Edit_BodegaADRView.as_view()), name="edit_bodega_adr"),
    

    #URL BODEGA_ADR (PAGINA CON TODOS LOS REGISTROS DE BODEGA ADR)
    path('bodega_adr/', login_required(BodegaADRView.as_view()), name="bodega_adr"),

    #URL PARA AGREGAR UN ACTIVO A LA AZOTEA DEL ADR
    path('add_azotea_adr/', login_required(AddAzoteaView.as_view()), name='add_azotea_adr'),

    #URL EDIT_AZOTEA (PAGINA PARA EDITAR UN REGISTRO DE AZOTEA)
    path('edit_azotea_adr/<int:pk>/', login_required(Edit_AzoteaView.as_view()), name='edit_azotea_adr'),

    #URL AZOTEA (PAGINA CON TODOS LOS REGISTROS DE AZOTEA)
    path('azotea_adr/', login_required(AzoteaView.as_view()), name="azotea_adr"),

    #URL PARA AGREGAR UN REGISTRO DE REPORTE DE UN ACTIVO
    path('add_reporte_equipos/', login_required(AddReporteView.as_view()), name='add_reporte_equipos'),

    #URL PARA LISTAR LOS EQUIPOS REPORTADOS
    path('reporte_equipos/', login_required(ReporteView.as_view()), name='reporte_equipos'),


    #URL PARA EL DETALLE DEL EQUIPO REPORTADO
    path('detail_reporte_equipo/<int:pk>/', login_required(ReporteEquipoDetailView.as_view()), name='detail_reporte_equipo'),

    #URL PARA EDITAR UN EQUIPO REPORTADO
    path('edit_reporte_equipo/<int:pk>/', login_required(EditReporteEquipoView.as_view()), name='edit_reporte_equipo'),

    #URL PARA LISTAR LA ENTREGA DE EQUIPOS
    path('entrega_equipos_reporte/', login_required(EntregaEquiposView.as_view()), name='entrega_equipos_reporte'),

    #URL PARA EDITAR LA ENTREGA DE EQUIPOS
    path('edit_entrega_equipo/<int:pk>/', login_required(EditEntregaEquipoView.as_view()), name='edit_entrega_equipo'),





    

]