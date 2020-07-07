from django.db import models
from user.models import UserProfile

# Create your models here.


class Likes(models.Model):
    sing = models.CharField(verbose_name="歌名", max_length=128)
    singer = models.CharField(verbose_name="歌手", max_length=50)
    status = models.IntegerField(verbose_name="收藏", default="已收藏")
    user_profile_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_likes"