from dataclasses import fields
from accounts.serializers import CompanySerializer, EmployeeSerializer
from rest_framework import serializers
from interviews.models import Interview

class InterviewSerializer(serializers.ModelSerializer):
    company_id=CompanySerializer
    employee_id=EmployeeSerializer
    class Meta:
        model=Interview
        fields="__all__"
        

         
class UpdateInterviewSerializer(serializers.ModelSerializer):
    class Meta:
         model=Interview
         fields=['job_title','description','questions','company_id','employee_id','answer']
         optional_fields=['job_title','description','questions','company_id','employee_id','answer']         