from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self,request):
        qs = Product.objects.all()

        brand_name = request.GET.get("brand_name")

        if brand_name:
            qs = qs.filter(brand_name=brand_name)

        limit = int(request.GET.get('limit', '10'))
        skip = request.GET.get('skip')

        if skip is None:
            print("sf")
            qs = qs[:limit]

        serializer = ProductSerializer(qs,many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product_obj = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(product_obj)
        return Response(serializer.data)

    def create(self,request):
        ## product sku can be auto genarated
        req_data = request.data
        serializer = ProductSerializer(data=req_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self,request,pk=None):
        print("delete")

        product_obj = get_object_or_404(Product,pk=pk)
        product_obj.delete()
        return Response(f"{pk} is deleted")

