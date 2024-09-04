
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")), # RECARGA LA PAGINA EN TIEMPO REAL CUANDO SE REALIZAN CAMBIOS
    path("accounts/", include("django.contrib.auth.urls")), # RUTAS DE AUTENTICACIÓN
    path('', include('adr.urls')),
]


# Configuración para servir archivos de medios en entornos de desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)