"""
project:
requirement:
author: BC
email: junzhou.nanijng@gmail.com
"""
from django.urls import path
from .views import UserView as user_view

urlpatterns = [
    # http://127.0.0.1:8000/v1/users/<username>
    path("<str:username>", user_view.as_view()),
]