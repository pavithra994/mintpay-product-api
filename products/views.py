from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status

# Create your views here.
from mintpay.utils import FinalResponse
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self,request):
        """
        product list service.
        service url: api/product/

        """
        qs = Product.objects.all()

        brand_name = request.GET.get("brand_name")

        if brand_name:
            qs = qs.filter(brand_name=brand_name)

        limit = int(request.GET.get('limit', '10'))
        skip = request.GET.get('skip')

        # product list limit will apply when 'skip' query parameter is null, else limit will be applied
        if skip is None:
            qs = qs[:limit]

        serializer = ProductSerializer(qs,many=True)

        return FinalResponse(status.HTTP_200_OK, data= serializer.data)

    def retrieve(self, request, pk=None):
        product_obj = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(product_obj)
        return FinalResponse(status.HTTP_200_OK, data= serializer.data)

    def create(self,request):
        # todo: product sku can be auto genarated
        req_data = request.data
        serializer = ProductSerializer(data=req_data)

        if serializer.is_valid():
            serializer.save()
            return FinalResponse(status.HTTP_201_CREATED, data= serializer.data)
        return FinalResponse(status.HTTP_400_BAD_REQUEST, errors= serializer.errors)

    def destroy(self,request,pk=None):

        product_obj = get_object_or_404(Product,pk=pk)
        product_obj.delete()
        return FinalResponse(status.HTTP_200_OK, message = f"{pk} is deleted")

