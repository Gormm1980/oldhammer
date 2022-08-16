from django.shortcuts import render
# Create your views here.

from rest_framework.response import Response
from Empire.api.serializers import Empire, EmpireCommanders, EmpireHeroes, EmpireBasicTroops, EmpireSpecialTroops, EmpireSingularTroops
from rest_framework import status, viewsets


class EmpireCommander(viewsets.ViewSet):
    def GET(self, request):
        commanders = EmpireCommanders.objects.all()
        serializer = EmpireCommandersSerializers(request.commanders)
        return Response(serializer.data)
    def POST(self, request):
        serializer = EmpireCommandersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def DELETE(self, request, pk):
        try:
            commanders = EmpireCommanders.objects.get(pk=pk)
        except commanders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        commanders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmpireHeroes(viewsets.ViewSet):
    def GET(self, request):
        heroes = EmpireHeroes.objects.all()
        serializer = EmpireHeroesSerializers(request.heroes)
        return Response(serializer.data)
    def POST(self, request):
        serializer = EmpireHeroesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def DELETE(self, request, pk):
        try:
            heroes = EmpireHeroes.objects.get(pk=pk)
        except heroes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        heroes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class  EmpireBasicTroops(viewsets.ViewSet):
        def GET(self, request):
            basic_troops = EmpireBasicTroops.objects.all()
            serializer = EmpireBasicTroopsSerializers(request.basic_troops)
            return Response(serializer.data)
        def POST(self, request):
            serializer = EmpireBasicTroopsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        def DELETE(self, request, pk):
            try:
                basic_troops = EmpireBasicTroops.objects.get(pk=pk)
            except basic_troops.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            basic_troops.delete()
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class EmpireSpecialTroops(viewsets.ViewSet):
        def GET(self, request):
            special_troops = EmpireSpecialTroops.objects.all()
            serializer = EmpireSpecialTroopsSerializers(request.special_troops)
            return Response(serializer.data)
        def POST(self, request):
            serializer = EmpireSpecialTroopsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        def DELETE(self, request, pk):
            try:
                special_troops = EmpireSpecialTroops.objects.get(pk=pk)
            except EmpireSpecialTroops.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            special_troops.delete()
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class EmpireSingularTroops(viewsets.ViewSet):
    def GET(self, request):
        singular_model = EmpireSingularModel.objects.all()
        serializer = EmpireSingularModelSerializers(singular_model)
        return Response(serializer.data)
    def POST(self, request):
        serializer = EmpireSingularModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def DELETE(self, request, pk):
        try:
            singular_model = EmpireSingularModel.objects.get(pk=pk)
        except singular_model.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        singular_model.delete()
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
    
class Empire(viewsets.ViewSet):
        def GET(self, request):
            empire = Empire.objects.all()
            serializer = EmpireSerializers(request.empire)
            return Response(serializer.data)
    