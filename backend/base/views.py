from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        "Hello Joon Saranghae"
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    #django restframework -> all models need to be serialized
    #serializer -> turns into Json format
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)

    for i in products:
        if i['_id'] == pk:
            product = i
            break

    return Response(serializer.data)
