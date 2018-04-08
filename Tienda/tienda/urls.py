
from django.conf.urls import url
from django.contrib import admin
from index import views

urlpatterns = [
    url(r'^$', views.plantilla_cargada),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.sesion),
    url(r'^gerencia/$', views.gerencial),
    url(r'^gerencia/logout/$', views.cerrar_sesion),
    url(r'^contactenos/$', views.mostrar_menu),
]
