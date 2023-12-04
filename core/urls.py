
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    # Base urls
    path('admin/', admin.site.urls),
    
    re_path('chaining/', include('smart_selects.urls')),
    
    # Local urls
    path("", include("apps.authentication.urls")),
    path("clientes/", include('apps.cliente.urls')),
    path("producto/", include('apps.antena.urls')),

    path("inicio", include("apps.home.urls")),
]

