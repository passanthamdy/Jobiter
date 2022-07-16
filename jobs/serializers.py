from rest_framework import serializers
from .models import Job,AppliedEmployees
from profiles.serializers import CompanySerializer


class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    # skills = TagSerializer(many=True)
    class Meta:
        model = Job
        fields = ['id', 'company', 'job_title', 'level', 'Description',
                  'job_type', 'work_type', 'salary', 'state',]
        optional_fields = [ 'state']
        depth = 1


class JobCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        exclude = ['company']
    


class JobUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['name', 'Tags', 'Description', 'status']
        optional_fields = ['name', 'skills', 'Description', 'status']

class AppliedEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppliedEmployees
        fields=['notice_period','cv','years_of_exp','cover_letter']
        depth=1
