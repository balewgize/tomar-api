from djoser.serializers import UserSerializer as BaseUserSerializer


class UserSerializer(BaseUserSerializer):
    """Custom serializer to ge the current user."""

    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name"]
