from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the category model."""

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "title", "slug"]


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the post model."""

    slug = serializers.SlugField(read_only=True)
    # category = serializers.StringRelatedField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "category", "user", "title", "content", "image", "slug"]

    def create(self, validated_data):
        user_id = self.context["user_id"]
        return Post.objects.create(user_id=user_id, **validated_data)
