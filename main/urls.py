from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view()),
    path('new/record/', views.RecordCreate.as_view(), name='new-record'),
    path('records/<int:user_id>/', views.RecordList.as_view(), name='records-list'),
    path('schedule/<int:coack_id>/', views.ScheduleList.as_view(), name='schedule-list'),
]




