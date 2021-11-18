from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for a profile model."""

    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ["user_id", "title", "bio", "avatar"]


class UserSerializer(BaseUserSerializer):
    """Custom serializer to ge the current user."""

    profile = ProfileSerializer()

    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name", "profile"]


class SimpleUserSerializer(BaseUserSerializer):
    """Expose few info about the user."""

    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username"]
