from django.shortcuts import render,redirect
from userapp.models import UserInfo,Ima1
from hashlib import sha1
from django.conf import settings
from django.http import HttpResponse
import os

# Create your views here.
list = []
list1 = []
list2 = []
def register(request):     #跳转注册页面
    return render(request,'register.html')


def register_handle(request): #注册判断用户输入
    namelist = UserInfo.objects.values_list('uname') #获取数据库里所有uname字段并返回一个列表
    print(namelist)
    uname = request.POST.get('user_name') #获取用户输入
    upwd = request.POST.get('pwd')
    upwd2 = request.POST.get('cpwd')
    uemail = request.POST.get('email')

    print(namelist)
    for i in namelist:      #遍历列表
        list2.append(i[0])  #把i的第0位索引循环追加到list2里
    if uname in list2:      #判断用户输入是否在list2 里
        return render(request, '存在.html')   #如果存在就返回存在的页面
    else:
        if upwd == upwd2: #否则就判断用户输入的密码和确认密码是否一致
            s1 = sha1()    #这三行是加入加密
            s1.update(upwd.encode('utf8'))
            upwd3 = s1.hexdigest()

            UserInfo.objects.create(uname=uname,upwd=upwd3,uemail=uemail) #如果一直就加入数据库,uname,upwd,uemail是字段名
            return render(request,'login.html')   #注册成功就返回登录页面

        else:
            return render(request,'两次不一致.html')#否则就返回两次输入不一致的页面

def tiao(request):    #从41行到63行没用，我自己瞎写的
    return render(request,'上传.html')
def chuan(request):
    pic1 = request.FILES.get('pic1')
    picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
    a = '/static/media/'

    picName1 = os.path.join(a,pic1.name)
    Ima1.objects.create(img=picName1)
    with open(picName, 'wb') as pic:
        for c in pic1.chunks():

            pic.write(c)
    return render(request,'显示图片.html',{'context':picName1})

def kan(request):
    a =Ima1.objects.all()
    print(a)


    return render(request,'显示图片.html',{'a':a})
def dengl(request):
    return render(request,'login.html')

def login(request): #登录判断
    booklist = UserInfo.objects.values_list('uname', 'upwd')  #代码跟注册差不多，都是判断用户输入和数据库里数据是否一致
    uname = request.POST['uname']
    upwd = request.POST['pwd']
    print(booklist)
    for i in booklist:
        list.append(i[0])
        list1.append(i[1])
    if uname in list:
        sy = list.index(uname)
        s1 = sha1()
        s1.update(upwd.encode('utf8'))
        upwd = s1.hexdigest()
        print(upwd)
        if upwd == list1[int(sy)]:
            request.session['uname'] = uname
            return redirect('/goods/index/')
        else:
            return HttpResponse("密码错误")
    else:
        return HttpResponse("不存在")

def tuichu(request):
    request.session.flush()
    return redirect('/user/dengl/')


        
