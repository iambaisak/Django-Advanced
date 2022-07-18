from rest_framework import serializers
from .models import Employee
from role.serializers import RoleSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','first_name','middle_name', 'last_name', 'mobile','date_created','date_updated')
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        self.fields['role'] = RoleSerializer(read_only=True)
        return super(EmployeeSerializer, self).to_representation(instance)