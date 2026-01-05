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
]
