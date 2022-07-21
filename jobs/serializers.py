import imp
from rest_framework import serializers
from .models import Job,AppliedEmployees
from profiles.serializers import CompanySerializer
from skills.serializers import SkillSerializer
from profiles.models import Company

class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)
    class Meta:
        model = Job
        fields = ['id', 'company', 'job_title', 'level', 'Description',
                  'job_type', 'work_type', 'salary', 'state','skills']
        optional_fields = [ 'state']
        depth = 1



class JobUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['job_title', 'level', 'Description',
                  'job_type', 'work_type', 'salary', 'skills']

class AppliedEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppliedEmployees
        fields=['notice_period','cv','years_of_exp','cover_letter']
        depth=1


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude=('company',)
   