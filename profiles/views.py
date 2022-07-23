import profile
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CompanySerializer,EmployeeSerializer
from .models import Company, Employee
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# Create your views here.
class RetrieveUpdateProfile(APIView):
    def get_object(self, pk,type):
        if type == "COMPANY":
            return Company.objects.get(pk=pk)
        elif type == "EMPLOYEE" :
            return Employee.objects.get(pk=pk)
    def get_serializer(self,type,query):
        if type == "COMPANY":
            return CompanySerializer(query)
        elif type == "EMPLOYEE":
            return EmployeeSerializer(query)
    
    def get(self, request, pk, format=None):
        user=User.objects.get(pk=pk)
        user_type=user.user_type
        print(pk,'>>',user_type)
        profile = self.get_object(pk,user_type)
        print(profile)
        serializer = self.get_serializer(user_type,profile)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user_type=request.user.user_type
        profile = self.get_object(pk,user_type)
        if request.user.id == pk:
            print("REQUEST USER ID >>> ", request.user.id)
            if user_type== "COMPANY":
                serializer = CompanySerializer(profile, data=request.data, partial=True)
            elif user_type == "EMPLOYEE":
                serializer = EmployeeSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({"details": "You don't have the persmission to update this profile"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"details": "your job cannot be edited "}, status=status.HTTP_400_BAD_REQUEST)



#allow notification
@api_view(["POST"])
def allow_notification(request):
    user = User.objects.get(pk=request.user.id)
    if user.allow_notification:
        user.allow_notification =False
        user.save()
    else:
        user.allow_notification =True
        user.save()
    return Response({'data': "Done"},status=status.HTTP_200_OK)



        
    
