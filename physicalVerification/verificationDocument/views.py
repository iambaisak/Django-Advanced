import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VerificationDocumentSerializer
from .models import VerificationDocument
from loanInformation.models import LoanApplication
from django.shortcuts  import get_object_or_404

class VerificationDocumentViews(APIView):
    def post(self, request):
        try:    
            loan_application_id=request.data.get("loan_application_id")
            data=request.data
            document_type=data.get('document_type')
            file_path=data.get('file_path')
            loan_application = LoanApplication.objects.get(id = loan_application_id)
            serializers = VerificationDocument.objects.create(document_type=document_type,file_path=file_path,loan_application=loan_application)    
            return Response({ "data": "success"})
        except:
            return Response({ "error": "failed"})

    def get(self, request, id=None):
        if id:
            item = VerificationDocument.objects.get(id=id)
            serializer = VerificationDocumentSerializer(item)
            return Response({ "data": serializer.data}, status= status.HTTP_200_OK)
        items = VerificationDocument.objects.all();
        serializer = VerificationDocumentSerializer(items, many=True)
        return Response({"error":serializer.data}, status= status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        if id:
            item = VerificationDocument.objects.get(id=id)
            serializer = VerificationDocumentSerializer(item, data=request.data, partial=True)
        if VerificationDocument.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response({"error": VerificationDocument.errors})

    def delete(self, request, id=None):
        item =get_object_or_404(VerificationDocument,  id=id)
        item.delete()
        return Response({"status": "item deleted"})
