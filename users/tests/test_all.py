import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybackend.settings')
import django
django.setup()

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import Usuario, Conexion
from users.views import agregar_usuario, agregar_conexion, usuarios_conectados, informe_estadistico



class UsuariosTests(APITestCase):
    def test_agregar_usuario(self):
        url = reverse(agregar_usuario)  # Corregir el nombre de la vista
        data = {'nombre': 'Test Usuario'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 1)
        self.assertEqual(Usuario.objects.get().nombre, 'Test Usuario')

    def test_agregar_conexion(self):
        usuario1 = Usuario.objects.create(nombre='Usuario 1')
        usuario2 = Usuario.objects.create(nombre='Usuario 2')
        url = reverse(agregar_conexion)  # Corregir el nombre de la vista
        data = {'usuario_origen': usuario1.id, 'usuario_destino': usuario2.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conexion.objects.count(), 1)

    def test_usuarios_conectados(self):
        usuario1 = Usuario.objects.create(nombre='Usuario 1')
        usuario2 = Usuario.objects.create(nombre='Usuario 2')
        Conexion.objects.create(usuario_origen=usuario1, usuario_destino=usuario2)
        url = reverse(usuarios_conectados, args=[usuario1.id])  # Corregir el nombre de la vista
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], 'Usuario 2')

    def test_informe_estadistico(self):
        # Crear usuarios y conexiones
        usuario1 = Usuario.objects.create(nombre='Usuario 1')
        usuario2 = Usuario.objects.create(nombre='Usuario 2')
        Conexion.objects.create(usuario_origen=usuario1, usuario_destino=usuario2)

        # Hacer solicitud a la vista de informe_estadistico
        url = reverse(informe_estadistico)
        response = self.client.get(url)

        # Verificar la respuesta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data

        # Verificar si el número de usuarios en los datos es correcto
        self.assertEqual(len(data), Usuario.objects.count())

        # Verificar si los datos de cada usuario son correctos
        for usuario_data in data:
            usuario_id = usuario_data['usuario_id']
            usuario = Usuario.objects.get(pk=usuario_id)
            self.assertEqual(usuario_data['nombre'], usuario.nombre)
            conexiones_salientes = [{'id': con.usuario_destino.id, 'nombre': con.usuario_destino.nombre} for con in Conexion.objects.filter(usuario_origen=usuario)]
            conexiones_entrantes = [{'id': con.usuario_origen.id, 'nombre': con.usuario_origen.nombre} for con in Conexion.objects.filter(usuario_destino=usuario)]
            self.assertEqual(usuario_data['conexiones_salientes'], conexiones_salientes)
            self.assertEqual(usuario_data['conexiones_entrantes'], conexiones_entrantes)