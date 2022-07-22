from rest_framework import serializers
from django.contrib.auth import get_user_model
from profiles.models import Company, Employee,City
from profiles.serializers import CitySerializer

User = get_user_model()


class SignupEmployeeSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password_confirm', 'gender','dob','image')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'gender': {'required': True},
            'dob':{'required': True},
            'image':{'required': True},

        }

    def save(self, **kwargs):
        employee = Employee(
            first_name=self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name'),
            username=self.validated_data.get('username'),
            email=self.validated_data.get('email'),
            gender=self.validated_data.get('gender'),
            dob=self.validated_data.get('dob'),
            image=self.validated_data.get('image'),
            user_type='EMPLOYEE',
            allow_notification=True,
            city_alert=False
        )
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {'confirm_password': "passwords didn't match"}
            )
        else:
            employee.set_password(self.validated_data.get('password'))
            employee.save()
            return employee


class SignupCompanySerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    # city = serializers.PrimaryKeyRelatedField(
    #     queryset=City.objects.all(),  write_only=True)
    class Meta:
        model = Company
        fields = (
        'username', 'email', 'company_name', 'city','address', 'about', 'industry', 'company_size', 'website', 'started_at',
        'password', 'password_confirm')
        extra_kwargs = {
            'company_name': {'required': True},
            'address': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'username': {'required': True},
            'industry':{'required': True},
            'about':{'required': True},
            'city':{'required': True},
        }

    def save(self, **kwargs):
        company = Company(
            username=self.validated_data.get('username'),
            address=self.validated_data.get('address'),
            email=self.validated_data.get('email'),
            company_name=self.validated_data.get('company_name'),
            about=self.validated_data.get('about'),
            industry=self.validated_data.get('industry'),
            company_size=self.validated_data.get('company_size'),
            city=self.validated_data.get('city'),
            website=self.validated_data.get('website'),
            started_at=self.validated_data.get('started_at'),
            user_type='COMPANY',
            allow_notification=True
        )
        print('username: ', company.username)
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {'confirm_password': "passwords didn't match"}
            )
        else:
            company.set_password(self.validated_data.get('password'))
            company.save()
            return company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'username', 'email', 'company_name', 'address', 'about', 'industry', 'company_size', 'website', 'started_at',
        'city')
