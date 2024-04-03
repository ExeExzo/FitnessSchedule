from rest_framework import serializers
from main.models import *


class RecordSerializer(serializers.ModelSerializer):
    user_first_name = serializers.SerializerMethodField()
    user_last_name = serializers.SerializerMethodField()
    coach_first_name = serializers.SerializerMethodField()
    coach_last_name = serializers.SerializerMethodField()
    gym_name = serializers.SerializerMethodField()
    gym_address = serializers.SerializerMethodField()
    gym_phone_number = serializers.SerializerMethodField()


    def get_user_first_name(self, obj):
        return obj.user.first_name
    
    def get_user_last_name(self, obj):
        return obj.user.last_name
    
    def get_coach_first_name(self, obj):
        return obj.coach.name
    
    def get_coach_last_name(self, obj):
        return obj.coach.surname
    
    def get_gym_name(self, obj):
        return obj.gym.name
    
    def get_gym_address(self, obj):
        return obj.gym.address
    
    def get_gym_phone_number(self, obj):
        return obj.gym.phone


    class Meta:
        model = Record
        fields = ['id', 'user', 'user_first_name', 'user_last_name', 'coach', 'coach_first_name', 'coach_last_name', 'gym', 'gym_name', 'gym_address', 'gym_phone_number', 'date', 'time', 'status', 'comment' ]
        read_only_fields = ['id', 'created', 'updated']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        read_only_fields = ['id', 'created', 'updated']