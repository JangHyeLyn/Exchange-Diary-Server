from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from rest_framework import status


class JWTTokenInvalidMiddleware(MiddlewareMixin):
    """
    check jwt token invalid
    """

    def process_request(self, request):
        headers = request.headers
        if 'Authorization' in headers:
            authorization = headers.get('Authorization')
            try:
                jwt_keword, token = authorization.split(' ')
            except Exception as e:
                data = {
                    "code": 401,
                    "message": "ERROR_INVALID_TOKEN",
                    "data": {
                        "detail": "invaild_jwt_token"
                    }
                }
                return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data=data)
        return None
