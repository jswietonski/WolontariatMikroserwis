from rest_framework.permissions import BasePermission


class HasPermission(BasePermission):
    permission = None

    """
    Użytkownik ma dostęp jezeli poosiada okreslone uprawniena
    """
    def has_permission(self, request, view):
        return request.auth and self.permission in request.auth.get('permissions', [])

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class HasAdminPermission(HasPermission):
    permission = "write:all_admin"


class HasOperatorPermission(HasPermission):
    permission = "write:operator"
