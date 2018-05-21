from django.shortcuts import render,redirect
from leongGoods.models import *
from django.core.paginator import *
# Create your views here.
import re
def index(request):
    a = GoodsInfo.objects.filter(gtype=1)
    a = a[0:4:1]
    b = GoodsInfo.objects.filter(gtype=2)
    b = b[0:4:1]
    c = GoodsInfo.objects.filter(gtype=3)
    c = c[0:4:1]
    d = GoodsInfo.objects.filter(gtype=4)
    d = d[0:4:1]
    e = GoodsInfo.objects.filter(gtype=5)
    e = e[0:4:1]
    f = GoodsInfo.objects.filter(gtype=6)
    f = f[0:4:1]
    a1 = TypeInfo.objects.filter(id=1)
    a2 = TypeInfo.objects.filter(id=2)
    a3 = TypeInfo.objects.filter(id=3)
    a4 = TypeInfo.objects.filter(id=4)
    a5 = TypeInfo.objects.filter(id=5)
    a6 = TypeInfo.objects.filter(id=6)
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
        context = {'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'a1':a1,'a2':a2,'a3':a3,'a4':a4,
                   'a5':a5,'a6':a6,'uname':uname,'uuu':uuu}
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'a1': a1,
                   'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5,'a6': a6, 'uname': uname,'uuu':uuu}
    return render(request,'index.html',context)
def cart(request):
    return render(request,'cart.html')



def gengduo(request,a,pindex='1'):

    print(a)
    if int(a) == 1:
        b = GoodsInfo.objects.filter(gtype=1)
        paginator = Paginator(b,1)
        page = paginator.page(int(pindex))
        c = '水果'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':page,'a':a,'c':c,'uname':uname,'uuu':uuu})
    elif int(a) == 2:
        b = GoodsInfo.objects.filter(gtype=2)
        paginator = Paginator(b, 1)
        page = paginator.page(int(pindex))
        c = '海鲜'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':page,'a':a,'c':c,'uname':uname,'uuu':uuu})
    elif int(a) == 3:
        b = GoodsInfo.objects.filter(gtype=3)
        paginator = Paginator(b, 1)
        page = paginator.page(int(pindex))
        c = '肉'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':page,'a':a,'c':c,'uname':uname,'uuu':uuu})
    elif int(a) == 4:
        b = GoodsInfo.objects.filter(gtype=4)
        paginator = Paginator(b, 1)
        page = paginator.page(int(pindex))
        c = '蛋'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':page,'a':a,'c':c,'uname':uname,'uuu':uuu})

    elif int(a) == 5:
        b = GoodsInfo.objects.filter(gtype=5)
        paginator = Paginator(b, 1)
        page = paginator.page(int(pindex))
        c =  '蔬菜'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':page,'a':a,'c':c,'uname':uname,'uuu':uuu})

    elif int(a) == 6:
        b = GoodsInfo.objects.filter(gtype=6)
        paginator = Paginator(b, 1)
        page = paginator.page(int(pindex))
        c = '冷饮'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':page,'a':a,'c':c,'uname':uname,'uuu':uuu})

def price(request,a):
    if int(a) == 1:
        b = GoodsInfo.objects.filter(gtype=1).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})
    elif int(a) == 2:
        b = GoodsInfo.objects.filter(gtype=2).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})
    elif int(a) == 3:
        b = GoodsInfo.objects.filter(gtype=3).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})

    elif int(a) == 4:
        b = GoodsInfo.objects.filter(gtype=4).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})

    elif int(a) == 5:
        b = GoodsInfo.objects.filter(gtype=5).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})

    elif int(a) == 6:
        b = GoodsInfo.objects.filter(gtype=6).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})

def moren(request,a):

    print(a)
    if int(a) == 1:
        b = GoodsInfo.objects.filter(gtype=1)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})
    elif int(a) == 2:
        b = GoodsInfo.objects.filter(gtype=2)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})
    elif int(a) == 3:
        b = GoodsInfo.objects.filter(gtype=3)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})

    elif int(a) == 4:
        b = GoodsInfo.objects.filter(gtype=4)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})

    elif int(a) == 5:
        b = GoodsInfo.objects.filter(gtype=5)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})

    elif int(a) == 6:
        b = GoodsInfo.objects.filter(gtype=6)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
        return render(request,'list.html',{'b':b,'a':a,'uname':uname,'uuu':uuu})

def detail(request):

    m = request.GET.get('a')
    d = request.GET.get('f', 1)
    b = GoodsInfo.objects.filter(id=int(m))
    print(m)
    print(b)
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
    return render(request,'detail.html',{'b':b,'d':d,'uname':uname,'uuu':uuu})

def jisuan(request,d):
    print(d)
    b = GoodsInfo.objects.filter(id=d)
    print(b)
    a = len(b)
    number = request.POST['number']
    price = request.POST['price']
    print(number,price)
    # number = int(number)
    # price = int(price)
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
    return render(request,'place_order.html',{'number':number,'price':price,'b':b,'a':a,'uname':uname,'uuu':uuu})

def cart(request):
    return render(request,'cart.html')

def jiaru(request,f):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
    else:
        return redirect('/user/dengl/')
    print(uname)
    unumber = f
    int(unumber)
    print(unumber)
    list = GoodsInfo.objects.filter(id = unumber)
    duixiang = list[0]
    print(duixiang)
    unumber = duixiang.id
    unumber = int(unumber)

    utitle = duixiang.gtitle
    udanjia = duixiang.gprice
    udanjia = float(udanjia)
    upic = duixiang.gpic
    print(upic)
    ushuliang = request.POST['ushuliang']
    print(ushuliang)
    # ushuliang = int(ushuliang)
    uprice = request.POST['uprice']
    uprice = float(uprice)
    Gouwu.objects.create\
    (uname=uname,utitle=utitle,ushu= ushuliang,uprice=uprice,unumber=unumber,udanjia=udanjia,upic=upic)
    return redirect('/goods/zhanshi')

def zhanshi(request):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
        chao = '<a href="/goods/zhanshi/">购物车</a>'
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/dengl/">购物车</a>'
    suoyou = Gouwu.objects.filter(uname=uname)
    print(suoyou)
    usum = 0
    for i in suoyou:
        usum += i.uprice
        print(usum)
    shu = len(suoyou)
    shu = int(shu)
    return render(request,'cart.html',
                  {'suoyou':suoyou,'shu':shu,'uname':uname,
                   'uuu':uuu,'chao':chao,'usum':usum})




