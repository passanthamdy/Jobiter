from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView

from profiles.models import Employee
from profiles.serializers import EmployeeSerializer
from .serializers import SkillSerializer
from .models import Skill
from rest_framework.response import Response


class HandleAllSkills(APIView):
    def get(self, request):
        skills_list = Skill.objects.all()
        serializer = SkillSerializer(skills_list, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )


class HandleEmployeeSkills(APIView):

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExists:
            raise Http404

    def get(self, request, pk):
        Employee = self.get_object(pk)
        serializer = EmployeeSerializer(Employee)
        return Response(serializer.data['skills'])

    def post(self, request, pk):
        Employee = self.get_object(pk)
        serializer = EmployeeSerializer(Employee)
        for skill in request.data:
            skill_obj = Skill.objects.get(id=skill)
            Employee.skills.add(skill_obj)
        return Response(serializer.data)

    def delete(self, request, pk):
        Employee = self.get_object(pk)
        serializer = EmployeeSerializer(Employee)
        for skill in request.data:
            skill_obj = Skill.objects.get(id=skill)
            Employee.skills.remove(skill_obj)
        return Response(serializer.data)
