from rest_framework import permissions
from userrole.models import *


class LibrarianPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        # return True if user has permission
        user = request.user
        role = RolesDefine.objects.get(user=user)
        if str(role.role) == "librarian":
            return True
        return False


class MemberPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        # return True if user has permission
        user = request.user.id
        print(user)
        role = RolesDefine.objects.get(user=user)
        print(str(role.role))
        if str(role.role) == "member":
            return True
