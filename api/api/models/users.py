
import random

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from api.models.base import BaseModel

def generate_invitation_no():
    now = timezone.now()
    no = f'{now.hour:02}{now.minute:02}{now.second:02}{now.microsecond // 1000}'
    return int(no)

class ValsRoomUserInvitation(BaseModel):
    no = models.IntegerField(default=generate_invitation_no, unique=True)

class ValsRoomUser(BaseModel):
    django_user = models.OneToOneField(User, on_delete=models.PROTECT)

    @property
    def is_admin(self):
        return self.django_user.is_staff
