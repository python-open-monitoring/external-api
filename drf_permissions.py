from rest_framework import permissions


class DrfApiPermission(permissions.BasePermission):
    """
    Global permission check
    """

    def has_permission(self, request, view):
        return True
