from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has a CustomUser first
        if not hasattr(request.user, 'customuser'):
            return False
        return request.user.customuser.is_superadmin()


class IsAdminLevel2OrAbove(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, 'customuser'):
            return False
        return request.user.customuser.is_superadmin() or request.user.customuser.is_admin2()


class IsStaffOrAbove(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, 'customuser'):
            return False
        return (
                request.user.customuser.is_superadmin() or
                request.user.customuser.is_admin2() or
                request.user.customuser.is_staff_member()
        )


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, 'customuser'):
            return False
        return request.user.customuser.is_student()
