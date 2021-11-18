from django.urls.conf import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register("posts", views.PostViewSet, basename="posts")
router.register("categories", views.CategoryViewSet, basename="categories")

urlpatterns = [
    path("", include(router.urls)),
]
