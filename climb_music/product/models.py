from django.db import models
from user.models import UserProfile

# Create your models here.


class Singer(models.Model):
    singer = models.CharField(verbose_name="歌手", max_length=50)


class Sing(models.Model):
    sing = models.CharField(verbose_name="歌名", max_length=50)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    issued_date = models.DateTimeField(verbose_name="发行日期")
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)



