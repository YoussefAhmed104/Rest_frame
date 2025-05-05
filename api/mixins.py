from .permissions import IsStaffEditorPermissions
from rest_framework import permissions

class StaffEsitorPermissionsMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermissions
        ]