
from django.db import transaction

from api.models.users import ValsRoomUserInvitation, ValsRoomUser, User

from api.services import exceptions

class UserCreateService:
    def create_user(
        self,
        *,
        invitation,
        username,
        password,
        name
    ):
        with transaction.atomic():
            try:
                inv = ValsRoomUserInvitation.objects.get(no=invitation)
            except ValsRoomUserInvitation.DoesNotExist:
                raise exceptions.ObjectNotFoundException()
            u = User.objects.create_user(
                username=username,
                password=password,
                first_name=name,
                is_staff=False
            )
            vru = ValsRoomUser.objects.create(
                django_user=u
            )
            return vru

class UserService:
    def __init__(self, user):
        self.user = user.valsroomuser

class ValsRoomUserInvitationsService(UserService):
    def generate_invitation(self):
        if not self.user.is_admin:
            raise exceptions.NotAuthorizedException()
        return ValsRoomUserInvitation.objects.create()

class UsersService:
    def __init__(self):
        pass