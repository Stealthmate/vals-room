
import logging

from api.permissions import IsAdmin

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models.users import ValsRoomUserInvitation
from api.services.users import ValsRoomUserInvitationsService, UserCreateService
from api.serializers.users import ValsRoomUserInvitationSerializer, RegisterUserSerializer
from api.permissions import IsAdmin

logger = logging.getLogger(__name__)

class UserInvitationViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = ValsRoomUserInvitation.objects.all()
    permission_classes = [ IsAuthenticated, IsAdmin ]
    serializer_class = ValsRoomUserInvitationSerializer
    lookup_field='no'

    def create(self, request):
        return Response(
            self.serializer_class(
                ValsRoomUserInvitationsService(request.user).generate_invitation()
            ).data
        )

class UserViewSet(viewsets.GenericViewSet):
    permission_classes = [ IsAuthenticated ]
    
    def get_permissions(self):
        logger.error(self.action)
        if self.action == 'register':
            return []
        return super().get_permissions()

    @action(methods=['POST'], detail=False, url_path='register')
    def register(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        UserCreateService().create_user(**serializer.validated_data)
        return Response()

    @action(methods=['GET'], detail=False, url_name='me', url_path='me')
    def me(self, request):
        return Response({ 'username': request.user.username, 'is_staff': request.user.is_staff })