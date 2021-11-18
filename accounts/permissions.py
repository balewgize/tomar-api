from rest_framework import permissions


class IsOwnerOfProfileOrReadOnly(permissions.BasePermission):
    """
    Custom Object-level permission to only allow owners of the profile to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
