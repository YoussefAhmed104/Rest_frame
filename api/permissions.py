from rest_framework import permissions

"""
Custom permission to only allow owners of an object to edit it.
"""
class IsStaffEditorPermissions(permissions.DjangoModelPermissions):
    """
    Custom permission to allow any member has acces to any fetuer to edit objects.
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }