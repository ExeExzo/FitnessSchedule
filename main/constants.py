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