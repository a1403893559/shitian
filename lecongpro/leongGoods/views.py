from django.shortcuts import render,redirect
from leongGoods.models import *
from django.core.paginator import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
shu = 0
from userapp.models import *
import random
import json
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
        chao = '<a href="/goods/zhanshi/">购物车</a>'
        zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
        dingdan = '<a href="/goods/dingdan/">全部订单</a>'
        suoyou = Gouwu.objects.filter(uname=uname)
        shu = len(suoyou)

        context = {'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'a1':a1,'a2':a2,'a3':a3,'a4':a4,
                   'a5':a5,'a6':a6,'dingdan':dingdan,'uname':uname,'uuu':uuu,'chao':chao,'zhongxin':zhongxin,'shu':shu}
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/dengl/">购物车</a>'
        zhongxin = '<a href="/user/dengl/">用户中心</a>'
        dingdan = '<a href="/user/dengl/">全部订单</a>'
        shu = []
        context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'a1': a1,
                   'a2': a2, 'a3': a3,'dingdan':dingdan, 'a4': a4, 'a5': a5,'a6': a6, 'uname': uname,'uuu':uuu,'chao':chao,'zhongxin':zhongxin}
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
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'b':page,'a':a,'c':c,
                                           'uname':uname,'dingdan':dingdan,'uuu':uuu,'shu':shu,'chao':chao,'zhongxin':zhongxin})
    elif int(a) == 2:
        b = GoodsInfo.objects.filter(gtype=2)
        paginator = Paginator(b, 1)
        page = paginator.page(int(pindex))
        c = '海鲜'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)

            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':page,'a':a,'c':c,
                                           'uname':uname,'uuu':uuu,'shu':shu,'chao':chao,'zhongxin':zhongxin})
    elif int(a) == 3:
        b = GoodsInfo.objects.filter(gtype=3)
        paginator = Paginator(b, 1)
        page = paginator.page(int(pindex))
        c = '肉'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':page,'a':a,'c':c,
                                           'uname':uname,'uuu':uuu,'shu':shu,'chao':chao,'zhongxin':zhongxin})
    elif int(a) == 4:
        b = GoodsInfo.objects.filter(gtype=4)
        paginator = Paginator(b, 1)
        page = paginator.page(int(pindex))
        c = '蛋'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':page,'a':a,'c':c,
                                           'uname':uname,'uuu':uuu,'shu':shu,'chao':chao,'zhongxin':zhongxin})

    elif int(a) == 5:
        b = GoodsInfo.objects.filter(gtype=5)
        paginator = Paginator(b, 1)
        page = paginator.page(int(pindex))
        c =  '蔬菜'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':page,'a':a,'c':c,
                                           'uname':uname,'uuu':uuu,'shu':shu,'chao':chao,'zhongxin':zhongxin})

    elif int(a) == 6:
        b = GoodsInfo.objects.filter(gtype=6)
        paginator = Paginator(b, 1)
        page = paginator.page(int(pindex))
        c = '冷饮'
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':page,'a':a,'c':c,
                                           'uname':uname,'uuu':uuu,'shu':shu,'chao':chao,'zhongxin':zhongxin})

def price(request,a):
    if int(a) == 1:
        b = GoodsInfo.objects.filter(gtype=1).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin,'shu':shu})
    elif int(a) == 2:
        b = GoodsInfo.objects.filter(gtype=2).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'shu':shu,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})
    elif int(a) == 3:
        b = GoodsInfo.objects.filter(gtype=3).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'shu':shu,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

    elif int(a) == 4:
        b = GoodsInfo.objects.filter(gtype=4).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'shu':shu,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

    elif int(a) == 5:
        b = GoodsInfo.objects.filter(gtype=5).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'shu':shu,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

    elif int(a) == 6:
        b = GoodsInfo.objects.filter(gtype=6).order_by('-gprice')
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
            suoyou = Gouwu.objects.filter(uname=uname)
            shu = len(suoyou)
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
            shu = []
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'shu':shu,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

def moren(request,a):

    print(a)
    if int(a) == 1:
        b = GoodsInfo.objects.filter(gtype=1)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})
    elif int(a) == 2:
        b = GoodsInfo.objects.filter(gtype=2)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})
    elif int(a) == 3:
        b = GoodsInfo.objects.filter(gtype=3)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})
    elif int(a) == 4:
        b = GoodsInfo.objects.filter(gtype=4)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

    elif int(a) == 5:
        b = GoodsInfo.objects.filter(gtype=5)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

    elif int(a) == 6:
        b = GoodsInfo.objects.filter(gtype=6)
        if request.session.get('uname') is not None:
            uname = request.session.get('uname')
            uuu = '<a href="/user/tuichu/">退出</a>'
            chao = '<a href="/goods/zhanshi/">购物车</a>'
            zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
            dingdan = '<a href="/goods/dingdan/">全部订单</a>'
        else:
            uname = '<a href="/user/dengl/">登录</a>'
            uuu = '<a href="/user/register/">注册</a>'
            chao = '<a href="/user/dengl/">购物车</a>'
            zhongxin = '<a href="/user/dengl/">用户中心</a>'
            dingdan = '<a href="/user/dengl/">全部订单</a>'
        return render(request,'list.html',{'dingdan':dingdan,'b':b,'a':a,'uname':uname,
                        'uuu':uuu,'chao':chao,'zhongxin':zhongxin})




def detail(request):

    m = request.GET.get('a')
    d = request.GET.get('f', 1)
    b = GoodsInfo.objects.filter(id=int(m))
    print(m)
    print(b)
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
        chao = '<a href="/goods/zhanshi/">购物车</a>'
        zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
        dingdan = '<a href="/goods/dingdan/">全部订单</a>'
        suoyou = Gouwu.objects.filter(uname=uname)
        shu = len(suoyou)
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/dengl/">购物车</a>'
        zhongxin = '<a href="/user/dengl/">用户中心</a>'
        dingdan = '<a href="/user/dengl/">全部订单</a>'
        shu = []
    return render(request,'detail.html',{'dingdan':dingdan,'b':b,'d':d,'uname':uname,'shu':shu,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})

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
        chao = '<a href="/goods/zhanshi/">购物车</a>'
        zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
        dingdan = '<a href="/goods/dingdan/">全部订单</a>'
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/dengl/">购物车</a>'
        zhongxin = '<a href="/user/dengl/">用户中心</a>'
        dingdan = '<a href="/user/dengl/">全部订单</a>'
    return render(request,'place_order.html',{'dingdan':dingdan,'number':number,'price':price,'b':b,'a':a,'uname':uname,'uuu':uuu,'chao':chao,'zhongxin':zhongxin})


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
    (uname=uname,utitle=utitle,ushu= ushuliang,uprice=uprice,
     unumber=unumber,udanjia=udanjia,upic=upic)
    return redirect('/goods/zhanshi')

def zhanshi(request):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
        chao = '<a href="/goods/zhanshi/">购物车</a>'
        zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
        dingdan = '<a href="/goods/dingdan/">全部订单</a>'
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/dengl/">购物车</a>'
        zhongxin = '<a href="/user/dengl/">用户中心</a>'
        dingdan = '<a href="/user/dengl/">全部订单</a>'
    suoyou = Gouwu.objects.filter(uname=uname)

    print(suoyou)
    usum = 0
    for i in suoyou:
        usum += i.uprice
        print(usum)
    shu = len(suoyou)
    shu = int(shu)
    return render(request,'cart.html',
                  {'suoyou':suoyou,'dingdan':dingdan,'shu':shu,'uname':uname,
                   'uuu':uuu,'chao':chao,'usum':usum,'zhongxin':zhongxin,'List':suoyou})

@csrf_exempt
def chuli(request):
    a = request.POST.get('a')
    a = int(a) + 1

    return JsonResponse({'a':a})

def tiaoyong(request):

    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
        chao = '<a href="/goods/zhanshi/">购物车</a>'
        zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
        dingdan = '<a href="/goods/dingdan/">全部订单</a>'
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/dengl/">购物车</a>'
        zhongxin = '<a href="/user/dengl/">用户中心</a>'
        dingdan = '<a href="/user/dengl/">全部订单</a>'
    dui = UserInfo.objects.filter(uname=uname)
    cc = dui[0]
    return render(request,'user_center_info.html',{'dingdan':dingdan,'uname':uname,'uuu':uuu,'chao':chao,'zhongxin':zhongxin,'cc':cc})


def gwjs(request):
    c = request.POST.get('c')
    price = request.POST.get('sum')
    c = list(c)
    a = []
    b = []
    for i in c:
        if i not in a:
            a.append(i)
    print(a)
    if len(a) >= 2:
        a.remove(',')
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
        chao = '<a href="/goods/zhanshi/">购物车</a>'
        zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
        dingdan = '<a href="/goods/dingdan/">全部订单</a>'
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/dengl/">购物车</a>'
        zhongxin = '<a href="/user/dengl/">用户中心</a>'
        dingdan = '<a href="/user/dengl/">全部订单</a>'
    suoyou = Gouwu.objects.filter(uname=uname)
    shu = len(a)
    for i in a:
        b.append(suoyou[int(i)])

    dui = UserInfo.objects.filter(uname=uname)
    cc = dui[0]

    return render(request,'gwjs.html',{'dingdan':dingdan,'uname':uname,'uuu':uuu,'chao':chao,
        'zhongxin':zhongxin,'b':b,'shu':shu,'price':price,'sum':price,'cc':cc,'a':a})


def dizhi(request):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
        chao = '<a href="/goods/zhanshi/">购物车</a>'
        zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
        dingdan = '<a href="/goods/dingdan/">全部订单</a>'
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/dengl/">购物车</a>'
        zhongxin = '<a href="/user/dengl/">用户中心</a>'
        dingdan = '<a href="/user/dengl/">全部订单</a>'
    dui = UserInfo.objects.filter(uname=uname)
    cc = dui[0]
    return render(request,'user_center_site.html',{'dingdan':dingdan,'uname':uname,
                    'uuu':uuu,'chao':chao,'zhongxin':zhongxin,'cc':cc})

def xiudi(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    youbian = request.POST.get('youbian')
    phone = request.POST.get('phone')
    if(len(phone)) != 11:
        return HttpResponse("手机号不对")
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
        chao = '<a href="/goods/zhanshi/">购物车</a>'
        zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
        dingdan = '<a href="/goods/dingdan/">全部订单</a>'
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/dengl/">购物车</a>'
        zhongxin = '<a href="/user/dengl/">用户中心</a>'
        dingdan = '<a href="/user/dengl/">全部订单</a>'
    dui = UserInfo.objects.filter(uname=uname)
    cc = dui[0]
    cc.ureceive = name
    cc.uaddress = address
    cc.uzip_code = youbian
    cc.uphone = phone
    cc.save()

    return render(request,'user_center_site.html',{'dingdan':dingdan,'uname':uname,
                    'uuu':uuu,'chao':chao,'zhongxin':zhongxin,'cc':cc})

def tijiao(request):
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')

    else:
        uname = '<a href="/user/dengl/">登录</a>'
    dui = UserInfo.objects.filter(uname=uname)
    cc = dui[0]
    aa = cc.uaddress
    print(aa)
    if cc.uaddress == '无' or cc.ureceive == '无' or cc.uphone == '无':
        return HttpResponse('资料不完整')
    else:
        a = request.POST.get('liebiao')
        price = request.POST.get('price')
        a = list(a)
        b = []
        c = []
        d = []
        for i in a:
            if i not in b:
                b.append(i)

        if len(b) >= 5:
            b.remove(' ')
            b.remove(',')
            b.remove("'")
            b.remove('[')
            b.remove(']')
        else:
            b.remove("'")
            b.remove('[')
            b.remove(']')

        suoyou = Gouwu.objects.filter(uname=uname)
        for i in b:

            c.append(suoyou[int(i)])

        suiji = random.randint(10000,99999)
        XD.objects.create(name=uname,danhao=suiji,zongjia=price)
        for i in c:
            Dingdan.objects.create(uname=i.uname,utitle=i.utitle,udanjia=i.udanjia,upic=i.upic
                               ,uprice=i.uprice,unumber=i.unumber,
                               ushu=i.ushu,dingdan=suiji,zongjia=price)
            d.append(i.id)
        for k in d:
            Gouwu.objects.filter(id=int(k)).delete()

        print('全都完成了')
        return redirect('/goods/dingdan/')

def dingdan(request):
    dlist = []
    xdlist = []
    if request.session.get('uname') is not None:
        uname = request.session.get('uname')
        uuu = '<a href="/user/tuichu/">退出</a>'
        chao = '<a href="/goods/zhanshi/">购物车</a>'
        zhongxin = '<a href="/goods/tiaoyong/">用户中心</a>'
        dingdan = '<a href="/goods/dingdan/">全部订单</a>'
    else:
        uname = '<a href="/user/dengl/">登录</a>'
        uuu = '<a href="/user/register/">注册</a>'
        chao = '<a href="/user/dengl/">购物车</a>'
        zhongxin = '<a href="/user/dengl/">用户中心</a>'
        dingdan = '<a href="/user/dengl/">全部订单</a>'

    xd = XD.objects.filter(name=uname).values_list('danhao')
    print(dlist)
    print(xd)
    for dd in xd:
        for xx in dd:
            xdlist.append(xx)
    print(xdlist)
    try:


        for i in xdlist:
            dui = Dingdan.objects.filter(uname=uname,dingdan=i)
            dlist.append({i:dui})
        print(dlist)

        return render(request, 'user_center_order.html',
                  {'dingdan':dingdan,'uname': uname, 'uuu': uuu,'chao': chao, 'zhongxin': zhongxin,
                'dlist':dlist})
    except:
        return HttpResponse('您还没有订单')