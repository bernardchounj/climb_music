"""
project:
requirement:
author: BC
email: junzhou.nanijng@gmail.com
"""
import jwt
from django.conf import settings
from django.http import JsonResponse

from user.models import UserProfile


def logging_check(func):
    def wrap(request, *args, **kwargs):
        # 请求头 - Authorization
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code': 403, 'error': 'Please login'}
            return JsonResponse(result)
        # 校验token
        try:
            res = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithm='HS256')
        except Exception as e:
            print('--check login error %s' % (e))
            result = {'code': 403, 'error': '--Please login!'}
            return JsonResponse(result)

        username = res['username']
        user = UserProfile.objects.get(username=username)
        request.myuser = user

        return func(request, *args, **kwargs)

    return wrap