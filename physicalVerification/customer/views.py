from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from .models import Customer
from django.shortcuts  import get_object_or_404
# Create your views here.

class CustomerViews(APIView):
    def post(self, request):
        serializers = CustomerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save();
            return Response({"data": serializers.data}, status= status.HTTP_200_OK)
        else:
            return Response({"error": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Customer.objects.get(id=id)
            serializer = CustomerSerializer(item)
            return Response({"data": serializer.data}, status= status.HTTP_200_OK)
        items = Customer.objects.all();
        serializer = CustomerSerializer(items, many=True)
        return Response({"data":serializer.data}, status= status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        if id:
            item = Customer.objects.get(id=id)
            serializer = CustomerSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response({"error": serializer.errors})

    def delete(self, request, id=None):
        item =get_object_or_404(Customer,  id=id)
        item.delete()
        return Response({"status": "item deleted"})
