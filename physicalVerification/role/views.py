from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RoleSerializer
from .models import Role
from django.shortcuts  import get_object_or_404

class RoleViews(APIView):
    def post(self, request):
        serializers = RoleSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"data": serializers.data}, status= status.HTTP_200_OK)
        else:
            return Response({"error": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Role.objects.get(id=id)
            serializer = RoleSerializer(item)
            return Response({"data": serializer.data}, status= status.HTTP_200_OK)
        items = Role.objects.all()
        serializer = RoleSerializer(items, many=True)
        return Response({"error":serializer.data}, status= status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        if id:
            item = Role.objects.get(id=id)
            serializer = RoleSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response({"error": serializer.errors})

    def delete(self, request, id=None):
        item =get_object_or_404(Role,  id=id)
        item.delete()
        return Response({"error": "item deleted"})

