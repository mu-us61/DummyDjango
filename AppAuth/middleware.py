from .models import MyUser


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.session.get("user_id")
        if user_id:
            try:
                request.user = MyUser.objects.get(id=user_id)
            except MyUser.DoesNotExist:
                request.user = None
        else:
            request.user = None
        return self.get_response(request)


def auth_middleware(get_response):
    def middleware(request):
        user_id = request.session.get("user_id")
        if user_id:
            try:
                request.user = MyUser.objects.get(id=user_id)
            except MyUser.DoesNotExist:
                request.user = None
        else:
            request.user = None

        response = get_response(request)
        return response

    return middleware
