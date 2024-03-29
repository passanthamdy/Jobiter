from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from salaries.models import Salary
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import SalarySerializer,SalaryCreateSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .permissions import MyPermission
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView
from accounts.models import User

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])  # IsAuthenticated,
@api_view(["GET"])
def salaries_list(request,id):
    company=User.objects.get(pk=id)
    salary_object = Salary.objects.filter(company=company)
    serializer = SalarySerializer(salary_object, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])  # IsAuthenticated,
@api_view(["GET"])
def salary_view(request, pk):
    salary_object = Salary.objects.get(pk=pk)
    serializer=SalarySerializer(salary_object)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, MyPermission])  # IsAuthenticated,
# @permission_classes([MyPermission]) #IsAuthenticated,
def salary_create(request,id):
    user_id=request.user.id
    company=User.objects.get(pk=id)
    employee=User.objects.get(pk=user_id)
    serializer = SalaryCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(company=company, reviewer=employee)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, MyPermission])  # IsAuthenticated,
def salary_delete(request, pk):
    Salary.objects.get(pk=pk).delete()
    return Response(data={'detail': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

