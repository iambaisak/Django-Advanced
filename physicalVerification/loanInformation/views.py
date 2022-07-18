from msilib.schema import Error
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoanApplicationSerializer
from .models import LoanApplication
from .serializers import LoanApplicationHistorySerializer
from .models import LoanApplicationHistory
from employee.models import Employee
from customer.models import Customer
from django.shortcuts import get_object_or_404
from django.shortcuts import render


# Create your views here.


class LoanApplicationViews(APIView):
    def post(self, request):
        try: 
            data=request.data
            status=data.get('status')
            verification_status=data.get('verification_status')
            loan_amount=data.get('loan_amount')
            customer_id=data.get("customer_id")
            customer = Customer.objects.get(id = customer_id)
            manager_id=data.get("manager_id")
            manager = Employee.objects.get(id = manager_id)
            verifier_id=data.get("verifier_id")
            verifier = Employee.objects.get(id = verifier_id)
            reviewer_id=data.get("reviewer_id")
            reviewer = Employee.objects.get(id = reviewer_id)
            if verification_status != "new" or status != "verification_pending":
                return Response({ "error": "The status of loan application must be verification_pending and verification_status should be new"})
            serializers = LoanApplication.objects.create(status=status,verification_status=verification_status,loan_amount=loan_amount,customer=customer,manager=manager,verifier=verifier,reviewer=reviewer)    
            return Response({ "data": "success"})
        except BaseException as e:
            return Response({"error": e})

    def get(self, request, id=None):
        if id:
            item = LoanApplication.objects.get(id=id)
            serializer = LoanApplicationSerializer(item)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        items = LoanApplication.objects.all();
        serializer = LoanApplicationSerializer(items, many=True)
        return Response({"error": serializer.data})

    def patch(self, request, id=None):
        if id:
            item = LoanApplication.objects.get(id=id)
            serializer = LoanApplicationSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response({"error": LoanApplication.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(LoanApplication, id=id)
        item.delete()
        return Response({"status": "item deleted"})


# Create your views here.

class LoanApplicationHistoryViews(APIView):
    def post(self, request):
        serializers = LoanApplicationHistorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save();
            return Response({"data": serializers.data}, status=status.HTTP_200_OK)
        else:
            return Response({"error": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = LoanApplicationHistory.objects.get(id=id)
            serializer = LoanApplicationHistorySerializer(item)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        items = LoanApplicationHistory.objects.all();
        serializer = LoanApplicationHistorySerializer(items, many=True)
        return Response({"error": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        if id:
            item = LoanApplicationHistory.objects.get(id=id)
            serializer = LoanApplicationHistorySerializer(item, data=request.data, partial=True)
        if LoanApplicationHistory.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response({"error": LoanApplicationHistory.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(LoanApplicationHistory, id=id)
        item.delete()
        return Response({"status": "item deleted"})