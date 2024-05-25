from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario, Conexion
from .serializers import UsuarioSerializer, ConexionSerializer

@api_view(['POST'])
def agregar_usuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def agregar_conexion(request):
    serializer = ConexionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def usuarios_conectados(request, usuario_id):
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
        conexiones_salientes = Conexion.objects.filter(usuario_origen=usuario)
        usuarios_conectados = [conexion.usuario_destino for conexion in conexiones_salientes]
        serializer = UsuarioSerializer(usuarios_conectados, many=True)
        return Response(serializer.data)
    except Usuario.DoesNotExist:
        return Response({"error": "El usuario no existe"}, status=404)
    
@api_view(['GET'])
def informe_estadistico(request):
    usuarios = Usuario.objects.all()
    data = []

    for usuario in usuarios:
        conexiones_salientes = Conexion.objects.filter(usuario_origen=usuario)
        conexiones_entrantes = Conexion.objects.filter(usuario_destino=usuario)
        
        conexiones_salientes_info = [{'id': con.usuario_destino.id, 'nombre': con.usuario_destino.nombre} for con in conexiones_salientes]
        conexiones_entrantes_info = [{'id': con.usuario_origen.id, 'nombre': con.usuario_origen.nombre} for con in conexiones_entrantes]
        
        usuario_data = {
            "usuario_id": usuario.id,
            "nombre": usuario.nombre,
            "conexiones_salientes": conexiones_salientes_info,
            "conexiones_entrantes": conexiones_entrantes_info
        }
        data.append(usuario_data)

    return Response(data)