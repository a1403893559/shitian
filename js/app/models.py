from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)  # 姓名
    upwd = models.CharField(max_length=40)  # 密码
    uemail = models.CharField(max_length=30)  # 邮箱


class LiuYan(models.Model):
    uname = models.CharField(max_length=20)
    name = models.CharField(max_length=20,default='')
    email = models.CharField(max_length=40,default='')
    address = models.CharField(max_length=40,default='')
    liuyan = models.CharField(max_length=300,default='')
