from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model
from experience.models import Experience


# User = get_user_model()


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        # fields = '__all__'
        fields = ('company_name', 'job_title', 'start_date', 'end_date', 'description','user')

#
# class ExperienceCreateSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Experience
#         # fields = '__all__'
#         fields = ('company_name', 'job_title', 'start_date', 'end_date', 'description',)
