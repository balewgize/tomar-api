from django.db.models.aggregates import Count
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Category, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CategorySerializer, PostSerializer


class CategoryViewSet(ModelViewSet):
    """Viewset that provide CURD+L  on categories for admin user."""

    http_method_names = ["get", "post", "put", "delete", "head", "options"]
    queryset = Category.objects.annotate(total_posts=Count("posts")).all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]


class PostViewSet(ModelViewSet):
    """Viewsets that prove CRUD+L operations on posts."""

    http_method_names = ["get", "post", "put", "delete", "head", "options"]
    queryset = Post.objects.select_related("category").all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in ["POST"]:
            return [IsAuthenticated()]
        elif self.request.method in ["PUT", "DELETE"]:
            return [IsAuthenticated(), IsAuthorOrReadOnly()]
        return [IsAuthorOrReadOnly()]

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
