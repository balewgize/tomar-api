from rest_framework import serializers

from accounts.serializers import SimpleUserSerializer
from .models import Category, Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the post model."""

    slug = serializers.SlugField(read_only=True)
    user = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "image", "slug", "category", "user"]

    def create(self, validated_data):
        user_id = self.context["user_id"]
        return Post.objects.create(user_id=user_id, **validated_data)


class SimplePostSerializer(serializers.ModelSerializer):
    """Expose few info about the posts."""

    class Meta:
        model = Post
        fields = ["id", "title", "slug", "user"]


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the category model."""

    slug = serializers.SlugField(read_only=True)
    posts = SimplePostSerializer(many=True)
    total_posts = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "title", "slug", "posts", "total_posts"]
