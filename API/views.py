from django.shortcuts import render

# Create your views here.
from .models import Turnos
from django.http import Http404

from API.serializers import TurnosSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

def index(request):
    #print 'Hi'
    #return HttpResponse("<script>document.write('HH');console.log('HHH')</script>Hello, world. You're at the turnos index.")
    Lista = Turnos.objects.all()
    context = {'Turnos': Lista}
    return render(request, 'index.html', context)

class TurnosList(APIView):
    def get(self, request, format=None):
        turnos = Turnos.objects.all()
        serializer = TurnosSerializer(turnos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.method)
        serializer = TurnosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        print(request.method)
        pk = request.data['id']
        turno = Turnos.objects.filter(id=pk)
        try:
            turno.delete()
            return Response(self.codigo, status = status.HTTP_200_OK)
        except:
            raise Http404

class TurnosDetail(APIView):
    def get_object(self, pk):
        try:
            return Turnos.objects.get(pk=pk)
        except Turnos.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        turno = self.get_object(pk)
        turno = TurnosSerializer(turno)
        return Response(turno.data)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        turno = self.get_object(pk)
        serializer = TurnosSerializer(turno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        turno = self.get_object(pk)
        turno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
