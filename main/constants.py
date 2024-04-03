from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Role(IntegerChoices):
    ADMIN = 1, _('admin')
    CLIENT = 2, _('client')
    COACH = 3, _('coach')
    GYM = 4, _('gym')


class Gender(IntegerChoices):
    NotSelected = 0, _('none')
    MALE = 1, _('male')
    FEMALE = 2, _("female")
    OTHER = 3, _("other")


class Status(IntegerChoices):
    PLANNED = 1, _('planned')
    DONE = 2, _('done')
    CANCELED = 3, _('canceled')
    CHANGED = 4, _('changed')


class DayOfWeek(IntegerChoices):
    MONDAY = 1, _('Monday')
    TUESDAY = 2, _('Tuesday')
    WEDNESDAY = 3, _('Wednesday')
    THURSDAY = 4, _('Thursday')
    FRIDAY = 5, _('Friday')
    SATURDAY = 6, _('Saturday')
    SUNDAY = 7, _('Sunday')