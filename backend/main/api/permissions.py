from django.conf import settings
from rest_framework import exceptions, permissions, status


class CustomPermission(permissions.BasePermission):
    """
    Permission subclass for custom request header validation
    """

    _missing_header_message = 'x-api-key header is missing'
    _invalid_header_message = 'x-api-key header is invalid'

    def has_permission(self, request, view):
        if settings.API_KEY_HEADER in request.headers:
            if request.headers[settings.API_KEY_HEADER] == settings.API_KEY:
                return True
            else:
                response = {
                    "message": self._invalid_header_message,
                }
                raise exceptions.PermissionDenied(detail=response, code=status.HTTP_401_UNAUTHORIZED)
        else:
            response = {
                "message": self._missing_header_message,
            }
            raise exceptions.PermissionDenied(detail=response, code=status.HTTP_403_FORBIDDEN)
