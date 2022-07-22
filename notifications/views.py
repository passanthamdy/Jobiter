import imp
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.response import Response


class ListNotifications(APIView):
   
    def get(self, request, format=None):
        """
        Return a list of all notifications related to the requested user.
        """
        
        notifications = Notification.objects.filter(user=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
