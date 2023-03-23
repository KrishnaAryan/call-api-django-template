from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

import requests
from django.shortcuts import render
def home(request):
    response=requests.get('http://127.0.0.1:8000/products').json()
    return render(request, 'product.html',{'response':response})