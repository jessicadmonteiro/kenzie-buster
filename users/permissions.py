from rest_framework import permissions


class PermissionsIdUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if obj.id == request.user.id and obj.is_employee is False:
            return True

        return request.user.is_authenticated and request.user.is_employee
