from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from app.models import *
from hashlib import sha1
from django.conf import settings
from django.http import HttpResponse

from django.http import HttpResponseRedirect

# Create your views here.
list = []
list1 = []
list2 = []


def register(request):  # 跳转注册页面
    return render(request, 'register.html')


def register_handle(request):  # 注册判断用户输入
    namelist = UserInfo.objects.values_list('uname')  # 获取数据库里所有uname字段并返回一个列表
    print(namelist)
    uname = request.POST.get('user_name')  # 获取用户输入
    upwd = request.POST.get('pwd')
    upwd2 = request.POST.get('cpwd')
    uemail = request.POST.get('email')

    print(namelist)
    for i in namelist:  # 遍历列表
        list2.append(i[0])  # 把i的第0位索引循环追加到list2里
    if uname in list2:  # 判断用户输入是否在list2 里
        return HttpResponse('已存在') # 如果存在就返回存在的页面
    else:
        if upwd == upwd2:  # 否则就判断用户输入的密码和确认密码是否一致
            s1 = sha1()  # 这三行是加入加密
            s1.update(upwd.encode('utf8'))
            upwd3 = s1.hexdigest()

            UserInfo.objects.create(uname=uname, upwd=upwd3, uemail=uemail)
            LiuYan.objects.create(uname=uname)
            # 如果一直就加入数据库,uname,upwd,uemail是字段名
            return render(request, 'login.html')  # 注册成功就返回登录页面

        else:
            return HttpResponse('两次不一致')  # 否则就返回两次输入不一致的页面


def dengl(request):
    return render(request, 'login.html')


def login(request):  # 登录判断
    booklist = UserInfo.objects.values_list('uname', 'upwd')  # 代码跟注册差不多，都是判断用户输入和数据库里数据是否一致
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
            return redirect('/goods/zhanshi')
        else:
            return HttpResponse("密码错误")
    else:
        return HttpResponse("不存在")


def tuichu(request):
    request.session.flush()
    return redirect('/user/dengl/')

def tiao(request):
    return render(request,'留言板.html')

def xieliu(request):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')
        duixiang = LiuYan.objects.filter(uname=uname)
        print(duixiang)
        aa = duixiang[0]
        aa.name = name
        aa.email = email
        aa.address = address
        aa.liuyan = message
        aa.save()
        return HttpResponseRedirect('/goods/zhanshi/')
    else:
        return HttpResponseRedirect('/goods/login/')

def zhanshi(request):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
    cc = LiuYan.objects.all()
    return render(request,'展示.html',{"cc":cc,'uname':uname})