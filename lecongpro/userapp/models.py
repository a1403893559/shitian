from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)  # 姓名
    upwd = models.CharField(max_length=40)  # 密码
    uemail = models.CharField(max_length=30)  # 邮箱
    ureceive = models.CharField(max_length=20, default='')  # 收件人
    uaddress = models.CharField(max_length=100, default='')  # 地址
    uzip_code = models.CharField(max_length=6, default='')  # 邮编
    uphone = models.CharField(max_length=11, default='')  # 手机

    # default,blank是Python层面的约束,不影响数据库表结构
class Ima1(models.Model):
    img = models.CharField(max_length=300)
