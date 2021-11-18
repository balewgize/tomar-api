from rest_framework import serializers

from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the category model."""

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "title", "slug"]


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the post model."""

    class Meta:
        model = Post
        fields = ["id", "category", "title", "content", "image"]
