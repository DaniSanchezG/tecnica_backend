from django.urls import path
from . import views

urlpatterns = [
    path('agregar_usuario/', views.agregar_usuario),
    path('agregar_conexion/', views.agregar_conexion),
    path('usuarios_conectados/<int:usuario_id>/', views.usuarios_conectados),
    path('informe_estadistico/', views.informe_estadistico)
]