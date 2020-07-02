import random
from django.db import models


# Create your models here.
def default_sign():
    """
    随机签名函数
    :return: 随机抽取一个字符串返回
    """
    signs = ["Great minds have purpose, others have wishes.",
             ]
    return random.choice(signs)


class UserProfile(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=11, editable=False, primary_key=True)
    nickname = models.CharField(verbose_name="昵称", max_length=30)
    # email = models.EmailField(default="NA")
    phone = models.CharField(max_length=11, default="")
    # qq = models.IntegerField(null=True)
    password = models.CharField(verbose_name="密码", max_length=32)

    sign = models.CharField(verbose_name="个人签名", max_length=50, default=default_sign)  # 可以随机制定一个函数
    info = models.CharField(verbose_name="个人描述", max_length=150, default="博主大人太懒了,什么也没留下~")

    avatar = models.ImageField(upload_to="avatar", null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_user_profile"