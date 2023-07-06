from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission


class SuperuserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class TokenPermission(BasePermission):
    def has_permission(self, request, view):
        if not "Authorization" in request.headers:
            return False
        auth_header =  request.headers['Authorization']
        if not auth_header.startswith("Token"):
            return False
        auth_header = auth_header.split(' ')
        if len(auth_header) != 2:
            return False
        if not Token.objects.filter(key=auth_header[1]).exists():
            return False
        return True
