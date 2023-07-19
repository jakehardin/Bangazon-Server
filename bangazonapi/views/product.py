"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Product


class ProductView(ViewSet):
    """DOCSTRING
    """

    def retrieve(self, request, pk):
        """DOCSTRING
        """
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def list(self, request):
        """DOCSTRING
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """DOCSTRING
        """

        product = Product.objects.create(
            name=request.data["name"],
            price=request.data["price"],
            image=request.data["image"],
            uid=request.data["uid"],
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk):
        """DOCSTRING
        """

        product = Product.objects.get(pk=pk)
        product.name = request.data["name"]
        product.price = request.data["price"]
        product.image = request.data["image"]

        product.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'image', 'uid')
