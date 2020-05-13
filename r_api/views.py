from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .models import Artical
from.serializer import ArticalSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def artical_list(request):
    if request.method == 'GET':
        artical = Artical.objects.all()
        serializer = ArticalSerializer(artical, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def artical_detail(request, pk):

    try:
        artical = Artical.objects.get(pk =  pk)
    except artical.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ArticalSerializer(artical)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticalSerializer(artical, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)
    elif request.method == 'DELETE':
        artical.delete()
        return HttpResponse(status=204)


