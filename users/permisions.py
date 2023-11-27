from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class PermissionCuston(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User):
        return request.user.is_superuser or user.email == request.user.email
