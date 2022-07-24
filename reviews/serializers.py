from dataclasses import fields
from profiles.serializers import CompanySerializer, EmployeeSerializer
from rest_framework import serializers
from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    company=CompanySerializer
    reviewer=EmployeeSerializer
    class Meta:
        model=Review
        fields="__all__"
        
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        exclude=('company','reviewer','employment_status')
        
class UpdateReviewSerializer(serializers.ModelSerializer):
    company=CompanySerializer
    reviewer=EmployeeSerializer
    class Meta:
        model=Review
        fields=["reviewer","company","pros","cons","employment_status","rating","is_published"]
        optional_fields=["reviewer","company","pros","cons","employment_status","rating","is_published"]

                