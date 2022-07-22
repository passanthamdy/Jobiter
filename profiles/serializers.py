from rest_framework import serializers

from skills.serializers import SkillSerializer
from .models import Company, City, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'username', 'email', 'company_name', 'address', 'about', 'industry',
                  'company_size', 'started_at', 'website', 'city', 'allow_notification', 'user_type','image')


class EmployeeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = Employee
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'gender', 'dob','image',
                  'city', 'level', 'job_title', 'city_alert', 'allow_notification', 'cv', 'user_type', 'skills')
                  
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields='__all__'