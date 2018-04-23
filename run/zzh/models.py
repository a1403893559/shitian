from django.db import models


class Biao(models.Model):
    title = models.CharField(max_length=20)
    nei = models.CharField(max_length=200)
    def __str__(self):
        return self.title
class Uname1(models.Model):
    yonghu = models.CharField(max_length=15)
    mima = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    qmima = models.CharField(max_length=25)
    wenti = models.CharField(max_length=25)
    daan = models.CharField(max_length=25)
