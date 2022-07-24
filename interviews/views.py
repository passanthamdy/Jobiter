from django.shortcuts import render
from rest_framework import status
from interviews.serializers import InterviewSerializer,UpdateInterviewSerializer,InterviewCreateSerializer
from interviews.models import Interview
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from interviews.permissions import MyPermission
from accounts.models import User

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_list_of_interviews(request,id):
        company=User.objects.get(pk=id)
        interviewsList=Interview.objects.filter(company_id=company)
        interviewsSerializer=InterviewSerializer(interviewsList,many=True)
        return Response(interviewsSerializer.data)

 
    
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,MyPermission ])    
def create_interview(request,id):
        user_id=request.user.id
        company=User.objects.get(pk=id)
        employee=User.objects.get(pk=user_id)
        interviewSerializer=InterviewCreateSerializer(data=request.data)
        if interviewSerializer.is_valid():
            interviewSerializer.save(company_id=company,employee_id=employee)
            return Response(interviewSerializer.data,status=status.HTTP_201_CREATED)
        return Response(interviewSerializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated ])
def interview_details(request, interview_id):
    interviewDetails = Interview.objects.get(pk=interview_id)
    interviewSerializer = InterviewSerializer(interviewDetails)
    return Response(data=interviewSerializer.data, status=status.HTTP_200_OK)

# @api_view(["DELETE"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated,MyPermission ])
# def delete_interview(request,interview_id):
#             interviewDetails = Interview.objects.get(pk=interview_id)
#             interviewDetails.delete()
#             return Response({"Message": "Interview Is Deleted Successfully"}, status=status.HTTP_200_OK)


# @api_view(["PUT","PATCH"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated,MyPermission ])
# def edit_interview(request,interview_id):
#         interviewDetails = Interview.objects.get(pk=interview_id)
#         interviewSerializer=UpdateInterviewSerializer(interviewDetails,data=request.data,partial=True)
#         if interviewSerializer.is_valid():
#                 interviewSerializer.save()
#                 return Response(interviewSerializer.data, status=status.HTTP_200_OK)
#         return Response({"Message": "Interview Is Not Updated  "}, status=status.HTTP_400_BAD_REQUEST)






