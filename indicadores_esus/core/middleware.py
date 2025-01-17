from django.utils.deprecation import MiddlewareMixin


class DisableCSRF(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/login/':
            setattr(request, '_dont_enforce_csrf_checks', True)