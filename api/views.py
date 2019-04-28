# api/views.py
# Import local objects
from api.models import Guest
from api.serializers import GuestSerializer

# Import Django packages
from django.shortcuts import render, get_object_or_404
from django.middleware.csrf import get_token
from django.http import HttpResponse, JsonResponse

# Django REST Framework imports and views
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework import generics, status, mixins

# For testing, use csrf_exempt decorator
from django.views.decorators.csrf import csrf_exempt

# REMOVE FOR PRODUCTION


@csrf_exempt
@api_view(['GET', 'POST'])
def guest_list(request, format=None):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
