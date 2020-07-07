from django.db import models

# Create your models here.
class Product(models.Model):
    sing = models.CharField(verbose_name="歌名", max_length=50)
    singer = models.CharField(verbose_name="歌手", max_length=50)
    issued_date = models.DateTimeField(verbose_name="发行日期")
