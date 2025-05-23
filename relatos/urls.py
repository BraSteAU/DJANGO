from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('acerca/', views.acerca, name='acerca'),
    path('relatos/', views.lista_relatos, name='lista_relatos'),
    path('relatos/agregar/', views.agregar_relato, name='agregar_relato'),
    path('relatos/<int:relato_id>/', views.detalle_relato, name='detalle_relato'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/agregar/', views.agregar_autor, name='agregar_autor' ),
]
=======
    path('',views.home,name='home'),
    path('acerca',views.acerca,name='acerca'),
    path('relatos/',views.lista_relatos,name='lista_relatos'),
    path('autores/',views.lista_autores,name='lista_autores'),
    path('autores/agregar/',views.agregar_autor,name='agregar_autor'),
    path('relatos/agregar/',views.agregar_relatos,name='agregar_relato'),
]
>>>>>>> 345886e3a7d9ea7681bba861300538be2f95f471
