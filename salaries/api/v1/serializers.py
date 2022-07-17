from rest_framework import serializers
from django.contrib.auth import get_user_model
from salaries.models import Salary

User = get_user_model()


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'
