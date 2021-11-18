from rest_framework.viewsets import ModelViewSet

from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer


class CategoryViewSet(ModelViewSet):
    """Viewset that provide CURD+L  on categories for admin user."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(ModelViewSet):
    """Viewsets that prove CRUD+L operations on posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        
        return super().create(request, *args, **kwargs)
