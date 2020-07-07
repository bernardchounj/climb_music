from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from like.models import Likes


# Create your views here.


class LikeView(View):
    def make_like(self, username):
        res = {"code": 200, "data": {}}
        likes = Likes.objects.filter(user_profile_id=username)
        for like in likes:
            res["id"] = like.id
            res["sing"] = like.sing
            res["singer"] = like.singer
            res["sstatus"] = like.status
        return res

    def make_listend(self, username):
        res = {"code": 200, "data": {}}
        likes = Likes.objects.filter(user_profile_id=username)
        for like in likes:
            res["id"] = like.id
            res["sing"] = like.sing
            res["singer"] = like.singer
            res["sstatus"] = like.status
        return res

    def make_bought(self, username):
        res = {"code": 200, "data":{}}


    def get(self, request, username):
        # http://127.0.0.1:8000/v1/users/bernard?like=1
        if request.GET.keys() == "like":
            res = self.make_like(username)
            return JsonResponse(res)
        # http://127.0.0.1:8000/v1/users/bernard?listend=1
        if request.GET.keys() == "listend":
            res = self.make_listend(username)
            return JsonResponse(res)
        # http://127.0.0.1:8000/v1/users/bernard?listend=1
        if request.GET.keys() == "bought":
            res = self.make_bought(username)
            return JsonResponse(res)

        if request.GET.keys() == "wallet":
            pass

