from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import PlantSerializer, FernSerializer, SucculentSerializer, VineSerializer,ShopperSerializer
from .models import Plant, Fern, Succulent, Vine, Shopper


class MyPlantSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('common_name')
    serializer_class = PlantSerializer

class MyFernSet(viewsets.ModelViewSet, APIView):
    queryset = Fern.objects.all().order_by('common_name')
    serializer_class = FernSerializer

class MySucculentSet(viewsets.ModelViewSet, APIView):
    queryset = Succulent.objects.all().order_by('common_name')
    serializer_class = SucculentSerializer

class MyVineSet(viewsets.ModelViewSet, APIView):
    queryset = Vine.objects.all().order_by('common_name')
    serializer_class = VineSerializer

class MyShopperSet(viewsets.ModelViewSet, APIView):
    queryset = Shopper.objects.all()
    serializer_class = ShopperSerializer

# Create your views here.
