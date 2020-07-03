import hashlib
import json
from django.http import JsonResponse
from django.views import View
from .models import UserProfile
from mtoken.views import make_token
# Create your views here.


class UserView(View):

    def get(self, request, username=None):
        json_str = request.body
        json_obj = json.loads(json_str)
        username = json_obj["username"]
        password = json_obj["password"]

        try:
            user = UserProfile.objects.get(username=username)
        except Exception as e:
            print(e)
            result = {"code": 10104, "error": "Your username or password is wrong, please try again"}
            return JsonResponse(result)

        if password != user.password:
            result = {"code": 10105, "error": "Your username or password is wrong, please try again"}
            return JsonResponse(result)
        else:
            result = {"code": 200, "username": user.username}
            return JsonResponse(result)




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

    def put(self, request, username):
        pass