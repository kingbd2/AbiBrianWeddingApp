# api/views.py
# Import local objects
from api.models import Guest, Party
from api.serializers import GuestSerializer, PartySerializer

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


@csrf_exempt
@api_view(['GET'])
def party_detail(request, invitation_id):
    """
    List party details.
    """
    party = Party.objects.get(
        invitation_id=invitation_id)
    serializer = PartySerializer(party)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def party_guests(request, invitation_id):
    """
    List guests in party.
    """
    if request.method == 'GET':
        party = Party.objects.get(
            invitation_id=invitation_id)
        guests = party.guest_set.all()
        # .values('last_name')
        serializer = GuestSerializer(guests, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT'])
def rsvp_guest(request, invitation_id, id):
    """
    View RSVP status and RSVP for guests in party.
    """
    if request.method == 'GET':
        guest = Guest.objects.get(id=id)
        serializer = GuestSerializer(guest)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        guest = Guest.objects.get(id=id)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
