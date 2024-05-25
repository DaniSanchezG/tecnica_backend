from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Conexion(models.Model):
    usuario_origen = models.ForeignKey(Usuario, related_name='conexiones_salientes', on_delete=models.CASCADE)
    usuario_destino = models.ForeignKey(Usuario, related_name='conexiones_entrantes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario_origen} -> {self.usuario_destino}'