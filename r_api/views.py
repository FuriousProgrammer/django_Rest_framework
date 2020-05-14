from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .models import Artical
from.serializer import ArticalSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


# Generic API Views
class GenericAPIViews(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.RetrieveModelMixin):
    queryset = Artical.objects.all()
    serializer_class = ArticalSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request, id=None):
        return self.create(request, id)

    def put(self, request, id=None):
        return self.update(request,id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


# Class Based API Views

class ArticalAPIView(APIView):

    def get(self, request):
        artical = Artical.objects.all()
        serializer = ArticalSerializer(artical,  many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Artical.objects.get(id=id)
        except Artical.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        artical = self.get_object(id)
        serializer = ArticalSerializer(artical)
        return Response(serializer.data)

    def put(self, request, id):
        artical = self.get_object(id)
        serializer = ArticalSerializer(artical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artical = self.get_object(id)
        artical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Functions Based API Views


@api_view(['GET', 'POST'])
def artical_list(request):
    if request.method == 'GET':
        artical = Artical.objects.all()
        serializer = ArticalSerializer(artical, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','DELETE'])
def artical_detail(request, pk):

    try:
        artical = Artical.objects.get(pk =  pk)
    except artical.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticalSerializer(artical)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticalSerializer(artical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        artical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


