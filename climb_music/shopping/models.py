from django.db import models
from product.models import Product
from user.models import UserProfile

# Create your models here.


class ShoppingHistory(models.Model):
    sing = models.ForeignKey(Product, on_delete=models.CASCADE)
    singer = models.ForeignKey(Product, on_delete=models.CASCADE)
    bought_time = models.DateTimeField(verbose_name="购买日期", auto_now_add=True)
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


