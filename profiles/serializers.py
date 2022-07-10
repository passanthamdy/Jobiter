from rest_framework import serializers
from .models import Company,City,Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','username','email','company_name', 'address', 'about','industry',
        'company_size','started_at','website','city', 'allow_notification', 'user_type')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields = ('id','username', 'first_name','last_name','email', 'gender','dob',
        'city','level','job_title','city_alert','allow_notification','cv','user_type')


