import hashlib
import json
from django.http import JsonResponse
from django.views import View

from like.models import Likes
from .models import UserProfile
from mtoken.views import make_token
from django.utils.decorators import method_decorator
from tools.logging_dec import logging_check
# Create your views here.


class UserView(View):
    def make_like(self, username):
        res = {"code": 200, "data": {}}
        likes = Likes.objects.filter(user_profile_id=username)
        for like in likes:
            res["id"] = like.id
            res["sing"] = like.sing
            res["singer"] = like.singer
            res["sstatus"] = like.status
        return res

    def get(self, request, username=None):
        # http://127.0.0.1:8000/v1/users/bernard?like=1
        for k in request.GET.keys():
            print(k)
        # print(key)
        # if key == "like":
        res = self.make_like(username)
        return JsonResponse(res)




    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        username = json_obj["username"]
        password_1 = json_obj["password_1"]
        password_2 = json_obj["password_2"]
        phone = json_obj["phone"]
        nickname = json_obj["nickname"]

        if len(username) > 32:
            result = {"code": 10100, "error": "The username is exceed length"}
            return JsonResponse(result)
        user = UserProfile.objects.filter(username=username)
        if user:
            result = {"code": 10101, "error": "The username is existed"}
            return JsonResponse(result)

        if password_1 != password_2:
            result = {"code": 10102, "error": "Please ensure passwords are complying"}
            return JsonResponse(result)
        p_m = hashlib.md5()
        p_m.update(password_1.encode())
        password_m = p_m.hexdigest()
        try:
            user = UserProfile.objects.create(username=username, password=password_m, phone=phone, nickname=nickname)
        except Exception as e:
            print("create user error %s" % e)
            result = {"code": 10103, "error": "The username is existed!"}
            return JsonResponse(result)

        token = make_token(username)
        result = {"code": 200, 'username': username, "data": {"token": token}}
        return JsonResponse(result)

    @method_decorator(logging_check)
    def put(self, request, username):
        # method_decorator 将传入的 函数装饰器 转换为 方法装饰器
        json_str = request.body
        json_obj = json.loads(json_str)

        request.myuser.sign = json_obj['sign']
        request.myuser.nickname = json_obj['nickname']
        request.myuser.info = json_obj['info']
        request.myuser.save()

        result = {'code': 200, 'username': request.myuser.username}
        return JsonResponse(result)