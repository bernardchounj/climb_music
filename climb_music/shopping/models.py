from django.db import models
from product.models import Singer, Sing
from user.models import UserProfile

# Create your models here.


class Bought(models.Model):
    sing = models.ForeignKey(Sing, on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    bought_time = models.DateTimeField(verbose_name="购买时间")
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


