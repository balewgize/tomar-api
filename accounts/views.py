from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=False, methods=["GET", "PUT"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Profile of a customer."""
        customer = Profile.objects.get(user_id=request.user.id)
        if request.method == "GET":
            serializer = ProfileSerializer(customer)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = ProfileSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
