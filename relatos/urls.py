from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('acerca',views.acerca,name='acerca'),
    path('relatos/',views.lista_relatos,name='lista_relatos'),
    path('autores/',views.lista_autores,name='lista_autores'),
    path('autores/agregar/',views.agregar_autor,name='agregar_autor'),
    path('relatos/agregar/',views.agregar_relatos,name='agregar_relatos'),
]