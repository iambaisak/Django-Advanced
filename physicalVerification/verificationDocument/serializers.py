from rest_framework import serializers
from .models import VerificationDocument
from loanInformation.serializers import LoanApplicationSerializer


class VerificationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationDocument
        fields = ('id', 'document_type', 'file_path','date_created','date_updated')

    def to_representation(self, instance):
        self.fields['loanApplication'] = LoanApplicationSerializer(read_only=True)
        return super(VerificationDocumentSerializer, self).to_representation(instance)