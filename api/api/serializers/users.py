
from rest_framework import serializers

from api.models.users import ValsRoomUserInvitation

class RegisterUserSerializer(serializers.Serializer):
    invitation = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()

class ValsRoomUserInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValsRoomUserInvitation
        read_only_fields = [
            'no'
        ]
        fields = [
            *read_only_fields,
        ]

class ValsRoomUserSerializer(serializers.Serializer):
    username = serializers.CharField(source='django_user.username')
    name = serializers.CharField(source='django_user.first_name')