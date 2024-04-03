from django.shortcuts import render
from rest_framework import generics
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status, views
from django.contrib.auth.models import User
from rest_auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *

class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class RecordCreate(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        client_id = request.data.get('client_id')
        coach_id = request.data.get('coach_id')
        gym_id = request.data.get('gym_id')
        
        client = get_object_or_404(User, pk=client_id)
        
        if user.role == Role.GYM:
            coach = get_object_or_404(Coach, pk=coach_id)
            gym = get_object_or_404(Gym, pk=gym_id)
            record = Record.objects.create(user=client, coach=coach, gym=gym, date=request.data.get('date'), time=request.data.get('time'), status=request.data.get('status'), comment=request.data.get('comment'))
            record.save()
            return Response({'message': 'Record created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You do not have permission to create a record'}, status=status.HTTP_403_FORBIDDEN)
        

class RecordList(LoggingMixin, generics.ListAPIView):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user_role = User.objects.get(id=user_id).role
        if user_role == Role.CLIENT:
            return Record.objects.filter(user=user_id)
        elif user_role == Role.COACH:
            return Record.objects.filter(coach=user_id)
        elif user_role == Role.GYM:
            return Record.objects.filter(gym=user_id)
        

class ScheduleList(LoggingMixin, generics.ListAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        coack_id = self.kwargs['coack_id']
        schedule = Schedule.objects.filter(Coach=coack_id)
        return schedule
        
