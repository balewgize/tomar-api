from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


from .models import Profile
from .permissions import IsOwnerOfProfileOrReadOnly
from .serializers import ProfileSerializer


class ProfileViewSet(
    ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    http_method_names = ["get", "put", "head", "options"]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOfProfileOrReadOnly]

    @action(detail=False, methods=["GET", "PUT"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Profile of the current authenticated user."""
        user_profile = Profile.objects.get(user_id=request.user.id)
        if request.method == "GET":
            serializer = ProfileSerializer(user_profile)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = ProfileSerializer(user_profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
