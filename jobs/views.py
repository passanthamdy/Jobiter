from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AppliedEmployeesSerializer, JobSerializer, JobUpdateSerializer, JobCreateSerializer
from jobs.models import Job,AppliedEmployees
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import generics
from profiles.models import Company, Employee
from django.core.exceptions import ObjectDoesNotExist
from notifications.models import Notification
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import MyPermission
# Create your views here.
"""
endpoints that performed by compnay user
"""
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, MyPermission, ])
def CreateJob(request):
    serializer = JobCreateSerializer(data=request.data,context={'request': request})
    user=request.user.id
    print('>>>>>',user)
    company=Company.objects.get(id=user)
    if serializer.is_valid():
        serializer.save(company=company)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, MyPermission, ])
def ListCompanyJobs( request):
        """
        Return a list of all jobs related to the requested user.
        """
        jobs = Job.objects.filter(company=request.user)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

class RetrieveUpdateDeleteCompanyJob(APIView):
    """
    get the job object 
    """
    permission_classes =(IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404
    """
    retrieve one job
    """
    def get(self, request, pk, format=None):
        print(request.user)
        job = self.get_object(pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)
    """
    Update job only if it's open and has permission to update it as a job owner 
    """
    def put(self, request, pk, format=None):
        
        job = self.get_object(pk)
        if request.user.id == job.company.id:
            serializer = JobUpdateSerializer(job, data=request.data, partial=True)
            print(request.data)
            if serializer.is_valid():
                print('vv')
                if job.state == "OPEN":
                    serializer.save()
                    return Response(serializer.data)
        else:
            return Response({"details": "You don't have the persmission to edit or delete this job"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"details": "your job cannot be edited "}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job = self.get_object(pk)
        st = status.HTTP_400_BAD_REQUEST
        if request.user.id == job.company.id:
            if job.state == 'OPEN':
                st = status.HTTP_204_NO_CONTENT
                job.delete()
                return Response({"details": "your job is deleted"}, status=st)
        else:
            return Response({"details": "You don't have the persmission to edit or delete this job"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"details": "job is not deleted"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, MyPermission, ])
def close_job(request,pk):
    job = Job.objects.get(id=pk)
    print(job.company.id,'>>>',request.user)
    if job.company.id == request.user.id:
            print('closed')
            job.state = 'CLOSED'
            job.save()
            return Response({"details":f"Your job is Finished"},status=status.HTTP_201_CREATED)
    return Response({"details": "You cannot close job that not related to your company"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, MyPermission, ])
def view_applicant(request,pk):
    app = AppliedEmployees.objects.get(pk=pk)
    if app.job.company.id == request.user.id:
        serializer = AppliedEmployeesSerializer(app)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response({"details": "You cannot check applicants that not belong to your job"}, status=status.HTTP_400_BAD_REQUEST)


"""
endpoint that get all the applied employees in certain job
""" 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, MyPermission, ])
def list_applied_employees(request,pk):
    job =Job.objects.get(pk=pk)
    if job.company.id == request.user.id:
        employees= AppliedEmployees.objects.get(job=job)
        serializer = AppliedEmployeesSerializer(employees)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response({"details": "You cannot list employees that does not belong to your jobs"}, status=status.HTTP_400_BAD_REQUEST)

"""
endpoints that performed by Employee users
"""

class ApplyForJob(APIView):
    permission_classes =(IsAuthenticated,)

    def post(self,request,pk,format=None):
        user=request.user.id
        employee=Employee.objects.get(id=user)
        job=Job.objects.get(id=pk)
        application=AppliedEmployees.objects.filter(job=job)
        for p in application:
            if p.employee.id == request.user.id:
                return Response({"details": "You applied to this job before"}, status=status.HTTP_400_BAD_REQUEST)
        if employee.user_type != 'EMPLOYEE':
            return Response({"details": "You're not allowed to apply to a job if you're not registered as employee"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AppliedEmployeesSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            notification=Notification.objects.create(
                    user=job.company, message="New employee applied to your job ",job=job,employee=employee
                )
            serializer.save(employee=employee,job=job)
          
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
endpoint that get all jobs that employee applied for
"""
@api_view(['GET'])
def list_applied_jobs(request):
    user=request.user.id
    employee=Employee.objects.get(id=user)
    jobs = AppliedEmployees.objects.get(employee=employee)
    serializer = AppliedEmployeesSerializer(jobs)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

class ListJobs(APIView):
    permission_classes =(IsAuthenticated,)
    def get(self,request,format=None):
        jobs= Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, MyPermission, ])
def accept_employee(request,job_id):
    user_id=request.data['id']
    job=Job.objects.get(pk=job_id)
    user=Employee.objects.get(id=user_id)
    print('USER>>>>>>>>',user)
    application = AppliedEmployees.objects.get(job=job,employee=user)
    serializer = AppliedEmployeesSerializer(application)
    if request.user.id == application.job.company.id:
        application.accepted ='True'
        application.save()
    else:
        return Response({"details": "You're not allowed to accept employees that don't belong to your job"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'details':"Developer has been accepted"}, status=status.HTTP_200_OK)



    
