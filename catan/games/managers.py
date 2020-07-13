from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'users.User')


class GameManager(models.Manager):
    """ Game manager """
    pass

