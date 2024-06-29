"""
URL configuration for AYUDANTIA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WEB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registrar_prestamo, name = 'registrar_prestamo'),
    path('registrar_empleado', views.registrar_empleado, name = 'registrar_empleado'),
    path('registrar_tipo_prestamo', views.registrar_tipo_prestamo, name = 'registrar_tipo_prestamo'),
    path('listar_prestamo', views.listar_prestamo, name = 'listar_prestamos'),
]