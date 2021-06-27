from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuario
from .serializers import UsuarioSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def lista_usuario(request):
    usuario = Usuario.objects.all()
    serializers = UsuarioSerializer(usuario, many=True)
    return Response(serializers.data)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def modificar_usuario(request):
    if request.method =='POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)
"""
@csrf_exempt
@api_view(['PUT'])
def actualizar_usuario(request,id):
    try:
        usuario = Usuario.objects.get(userName=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)

"""     

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated))
def actualizar_usuario(request,id):
    try:
        usuario = Usuario.objects.get(userName=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

