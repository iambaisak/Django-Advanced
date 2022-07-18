from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from .models import Employee
from role.models import Role
from django.shortcuts  import get_object_or_404

class EmployeeViews(APIView):
    def post(self, request):
        try:    
            role_id=request.data.get("role_id")
            data=request.data
            first_name=data.get('first_name')
            middle_name=data.get('middle_name')
            last_name=data.get('last_name')
            mobile=data.get('mobile')
            role = Role.objects.get(id = role_id)
            serializers = Employee.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,mobile=mobile,role=role)    
            return Response({"data": "success"}, status= status.HTTP_200_OK)
        except:
            return Response({"error": "failed"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(item)
            return Response({"data": serializer.data}, status= status.HTTP_200_OK)
        items = Employee.objects.all()
        serializer = EmployeeSerializer(items, many=True)
        return Response({"data":serializer.data}, status= status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        if id:
            item = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response({"error": serializer.errors})

    def delete(self, request, id=None):
        item =get_object_or_404(Employee,  id=id)
        item.delete()
        return Response({"status": "item deleted"})