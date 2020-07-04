import hashlib
import json
import time
import jwt
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from user.models import UserProfile

# Create your views here.



class TokenView(View):
    def post(self, request):
        # 获取用户名和密码
        json_str = request.body
        json_obj = json.loads(json_str)
        username = json_obj["username"]
        password = json_obj["password"]
        # 校验用户名和密码
        try:
            old_user = UserProfile.objects.get(username=username)
        except Exception as e:
            print(e)
            result = {"code": 10200, "error": "Your username or password are not correct, please try again"}
            return JsonResponse(result)
        hpassword = hashlib.md5()
        hpassword.update(password.encode())
        if hpassword.hexdigest() != old_user.password:
            result = {"code": 10201, "error": "Your username or password are not correct, please try again"}
            return JsonResponse(result)
        # 校验成功后 签发token 有效期一天
        token = make_token(username)
        result = {"code": 200, "username": username, "data":{"token": token.decode()}}
        return JsonResponse(result)


def make_token(username, expire=3600*24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {
        "username": username,
        "exp": now + expire,
    }
    return jwt.encode(payload, key, algorithm="HS256")
