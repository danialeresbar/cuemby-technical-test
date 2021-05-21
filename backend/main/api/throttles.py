from django.conf import settings
from rest_framework import exceptions, throttling


class CustomThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        headers = request.META
        return headers.get(settings.REST_API_KEY[0], '') == settings.REST_API_KEY[1]
