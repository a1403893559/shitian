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
def register(request):
    return render(request,'register.html')


def register_handle(request):
    namelist = UserInfo.objects.values_list('uname')
    print(namelist)
    uname = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    upwd2 = request.POST.get('cpwd')
    uemail = request.POST.get('email')

    print(namelist)
    for i in namelist:
        list2.append(i[0])
    if uname in list2:
        return render(request, '存在.html')
    else:
        if upwd == upwd2:
            s1 = sha1()
            s1.update(upwd.encode('utf8'))
            upwd3 = s1.hexdigest()

            UserInfo.objects.create(uname=uname,upwd=upwd3,uemail=uemail)
            return render(request,'login.html')

        else:
            return render(request,'两次不一致.html')

def tiao(request):
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

def login(request):
    booklist = UserInfo.objects.values_list('uname', 'upwd')
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
            return render(request,'index.html')
        else:
            return HttpResponse(request,'密码错误')



        
