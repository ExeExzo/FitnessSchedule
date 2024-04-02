from django.contrib import admin
from .models import *
from common.models import Base
# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    list_display = ['order', 'created', 'updated', 'is_active', 'is_deleted']
    list_filter = ['is_active', 'is_deleted']
    search_fields = ['name', 'description']
    ordering = ['order', 'created']


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'role', 'gender', 'date_of_birth', 'phone']
    list_filter = ['role']
    search_fields = ['name', 'surname', 'phone']


class GymAdmin(BaseAdmin):
    list_display = ['name', 'address', 'phone', 'email'] + BaseAdmin.list_display
    search_fields = ['name', 'address', 'phone', 'email']


class CoachAdmin(BaseAdmin):
    list_display = ['name', 'surname', 'date_of_birth', 'gender', 'gym', 'salary', 'date_of_start_working'] + BaseAdmin.list_display
    search_fields = ['name', 'surname', 'gym', 'salary']
    

class ScheduleAdmin(BaseAdmin):
    list_display = ['Coach', 'day_of_week', 'time_of_work'] + BaseAdmin.list_display
    search_fields = ['Coach', 'day_of_week', 'time_of_work']


class RecordAdmin(BaseAdmin):
    list_display = ['user', 'coach', 'gym', 'date', 'time', 'status', 'comment'] + BaseAdmin.list_display
    search_fields = ['user', 'coach', 'gym', 'date', 'time', 'status', 'comment']


admin.site.register(User, UserAdmin)
admin.site.register(Gym, GymAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Record, RecordAdmin)
