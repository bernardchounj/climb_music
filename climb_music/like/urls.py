"""
project:
requirement:
author: BC
email: junzhou.nanijng@gmail.com
"""
from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/v1/users/like/bernard
    path("<str:username>", views.LikeView.as_view()),
]
