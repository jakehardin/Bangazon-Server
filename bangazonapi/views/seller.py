"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Seller


class SellerView(ViewSet):
    """DOCSTRING
    """

    def retrieve(self, request, pk):
        """DOCSTRING
        """
        seller = Seller.objects.get(pk=pk)
        serializer = SellerSerializer(seller)
        return Response(serializer.data)


    def list(self, request):
        """DOCSTRING
        """
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)


    def destroy(self, request, pk):
        seller = Seller.objects.get(pk=pk)
        seller.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SellerSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Seller
        fields = ('id', 'uid', 'seller_id', 'name', 'profile_image_url', 'email')
