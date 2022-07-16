from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AppliedEmployeesSerializer, JobSerializer, JobUpdateSerializer, JobCreateSerializer
from jobs.models import Job,AppliedEmployees
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import generics
from profiles.models import Company, Employee
# Create your views here.

class ListCompanyJobs(APIView):
   
    def get(self, request, format=None):
        """
        Return a list of all jobs related to the requested user.
        """
        jobs = Job.objects.filter(company=request.user)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = JobCreateSerializer(data=request.data, context={'request': request})
        user=request.user.id
        company=Company.objects.get(id=user)
        if serializer.is_valid():
            serializer.save(company=company)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListJobs(APIView):
    def get(self,request,format=None):
        jobs= Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

class RetrieveUpdateDeleteCompanyJob(APIView):
    """
    get the job object 
    """
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
        if request.user == job.company:
            serializer = JobUpdateSerializer(job, data=request.data, partial=True)
            if serializer.is_valid():
                if job.state == "OPEN":
                    serializer.save()
                    return Response(serializer.data)
        else:
            return Response({"details": "You don't have the persmission to edit or delete this job"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"details": "your job cannot be edited "}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job = self.get_object(pk)
        st = status.HTTP_400_BAD_REQUEST
        if request.user == job.company:
            if job.state == 'OPEN':
                print('got delete')
                st = status.HTTP_204_NO_CONTENT
                job.delete()
                return Response({"details": "your job is deleted"}, status=st)
        else:
            return Response({"details": "You don't have the persmission to edit or delete this job"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"details": "job is not deleted"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def close_job(request,pk):
    job = Job.objects.get(id=pk)
    print("Comp >>>", job.company.id)
    print("USER >>>", request.user.id)
    if job.company.id == request.user.id:
        print("inside if>>>>")
        job.state = 'CLOSED'
        job.save()
        return Response({"details":f"Your job is Finished"},status=status.HTTP_201_CREATED)
    return Response({"details": "You cannot close job that not related to your company"}, status=status.HTTP_400_BAD_REQUEST)

class ApplyForJob(APIView):
    def post(self,request,pk,format=None):
        user=request.user.id
        employee=Employee.objects.get(id=user)
        job=Job.objects.get(id=pk)
        print(">>>>>>",employee.user_type)
        if employee.user_type != 'EMPLOYEE':
            return Response({"details": "You're not allowed to apply to a job if you're not registered as employee"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AppliedEmployeesSerializer(data=request.data)
        if serializer.is_valid():
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
"""
endpoint that get all the applied employees in certain job
"""
@api_view(['GET'])
def list_applied_employees(request,pk):
    job =Job.objects.get(pk=pk)
    employees= AppliedEmployees.objects.get(job=job)
    serializer = AppliedEmployeesSerializer(employees)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

