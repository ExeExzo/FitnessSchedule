from django.db import models
from common.models import Base
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from main.constants import *
from django.utils import timezone


class User(AbstractUser):
    role = models.PositiveIntegerField(
        verbose_name=_('Role'),
        choices=Role.choices,
        default=Role.CLIENT,
    )
    gender = models.PositiveIntegerField(
        verbose_name=_('Gender'),
        choices=Gender.choices,
        default=Gender.NotSelected,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(verbose_name=_('Phone number'), max_length=12)

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Gym(Base):
    name = models.CharField(verbose_name=_('Name of Gym'), blank=False, max_length=255)
    address = models.CharField(verbose_name=_('Address of Gym'), blank=False, max_length=255)
    phone = models.CharField(verbose_name=_('Phone number'), max_length=12)
    email = models.EmailField(verbose_name=_('Email of Gym'), max_length=255)

    class Meta:
        verbose_name_plural = _('Gym')


class Coach(Base):
    name = models.CharField(verbose_name=_('Name of Coach'), blank=False, max_length=255)
    surname = models.CharField(verbose_name=_('Surname of Coach'), blank=False, max_length=255)
    date_of_birth = models.DateField()
    gender = models.PositiveIntegerField(
        verbose_name=_('Gender'),
        choices=Gender.choices,
        default=Gender.NotSelected,
    )
    gym = models.ForeignKey(Gym , on_delete=models.CASCADE, verbose_name=_('Gym'), related_name='coaches', blank=False, null=False)
    salary = models.FloatField()
    date_of_start_working = models.DateField()

    class Meta:
        verbose_name_plural = _('Coach')


class Schedule(Base):
    Coach = models.ForeignKey(Coach, on_delete=models.CASCADE, verbose_name=_('Coach'), related_name='schedule_coach', blank=False, null=False)
    DayOfWeek = models.PositiveIntegerField(
        verbose_name=_('Day of the week'),
        choices=DayOfWeek.choices,
        default=DayOfWeek.MONDAY,
    )
    start_of_work = models.TimeField(verbose_name=_('start of the work'), blank=False, null=False)
    end_of_work = models.TimeField(verbose_name=_('end of the work'), blank=False, null=False)


class Record(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='user_records', blank=False, null=False)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, verbose_name=_('Coach'), related_name='record_coach', blank=False, null=False)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, verbose_name=_('Gym'), related_name='gym', blank=False, null=False)
    date = models.DateField()
    time = models.TimeField(verbose_name=_('Time'), blank=False, null=False)
    status = models.PositiveIntegerField(
        verbose_name=_('Status'),
        choices=Status.choices,
        default=Status.PLANNED,
    )
    comment = models.TextField(verbose_name=_('Comment'), blank=True, null=True)