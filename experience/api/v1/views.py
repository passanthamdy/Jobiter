from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from experience.models import Experience
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import ExperienceSerializer,ExperienceCreateSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .permissions import MyPermission
from accounts.models import User


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])  # IsAuthenticated,
@api_view(["GET"])
def experiences_list(request,id):
    user_obj=User.objects.get(id=id)
    experience_object = Experience.objects.filter(user=user_obj)
    serializer = ExperienceSerializer(experience_object,many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])  # IsAuthenticated,
def experience_create(request,id):
    serializer = ExperienceCreateSerializer(data=request.data, context={'request': request})
    user=request.user
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

