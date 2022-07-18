from rest_framework import serializers
from .models import LoanApplication
from customer.serializers import CustomerSerializer
from employee.serializers import EmployeeSerializer
from .models import LoanApplicationHistory


class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = (
            'id', 'status', 'verification_status', 'loan_amount', 'date_created',
            'date_updated')

    def to_representation(self, instance):
        self.fields['customer'] = CustomerSerializer(read_only=True)
        self.fields['employee'] = EmployeeSerializer(read_only=True)
        self.fields['reviewer'] = EmployeeSerializer(read_only=True)
        self.fields['manager'] = EmployeeSerializer(read_only=True)
        return super(LoanApplicationSerializer, self).to_representation(instance)


class LoanApplicationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplicationHistory
        fields = ('id','customer_id', 'status','verification_status', 'manager_id', 'verifier_id','reviewer','loan_amount','date_created','date_updated')

    def to_representation(self, instance):
        self.fields['loanApplication'] = LoanApplicationSerializer(read_only=True)
        return super(LoanApplicationHistorySerializer, self).to_representation(instance)
