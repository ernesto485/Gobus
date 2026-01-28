from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Autobus CRUD URLs
    path('autobuses/', views.autobus_list, name='autobus_list'),
    path('autobuses/crear/', views.autobus_create, name='autobus_create'),
    path('autobuses/<int:pk>/', views.autobus_detail, name='autobus_detail'),
    path('autobuses/<int:pk>/editar/', views.autobus_edit, name='autobus_edit'),
    path('autobuses/<int:pk>/eliminar/', views.autobus_delete, name='autobus_delete'),
    
    # Ruta CRUD URLs
    path('rutas/', views.ruta_list, name='ruta_list'),
    path('rutas/crear/', views.ruta_create, name='ruta_create'),
    path('rutas/<int:pk>/', views.ruta_detail, name='ruta_detail'),
    path('rutas/<int:pk>/editar/', views.ruta_edit, name='ruta_edit'),
    path('rutas/<int:pk>/eliminar/', views.ruta_delete, name='ruta_delete'),
    
    # Conductor CRUD URLs
    path('conductores/', views.conductor_list, name='conductor_list'), 
    path('conductores/crear/', views.conductor_create, name='conductor_create'), 
    path('conductores/<int:pk>/', views.conductor_detail, name='conductor_detail'),
    path('conductores/<int:pk>/editar/', views.conductor_edit, name='conductor_edit'), 
    path('conductores/<int:pk>/eliminar/', views.conductor_delete, name='conductor_delete'), 

    # Billetes CRUD URLs
    path('billetes/', views.billete_list, name='billete_list'),
    path('billetes/crear/', views.billete_create, name='billete_create'),
    
    path('billetes/<int:pk>/editar/', views.billete_edit, name='billete_edit'),
    
    path('billetes/<int:pk>/eliminar/', views.billete_delete, name='billete_delete'),
    
    path('billetes/<int:pk>/', views.billete_detail, name='billete_detail'),


]
