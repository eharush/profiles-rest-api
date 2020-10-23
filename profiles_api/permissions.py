from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        print(f'request.method = {request.method}')
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
