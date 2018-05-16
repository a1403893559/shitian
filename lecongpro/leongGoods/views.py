from django.shortcuts import render
from leongGoods.models import *
# Create your views here.
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

    context = {'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'a1':a1,'a2':a2,'a3':a3,'a4':a4,'a5':a5,'a6':a6}
    return render(request,'index.html',context)
def cart(request):
    return render(request,'cart.html')
def detail(request):
    return render(request,'detail.html')

def gengduo(request,a):

    print(a)
    if int(a) == 1:
        b = GoodsInfo.objects.filter(gtype=1)
        return render(request,'list.html',{'b':b,'a':a})
    elif int(a) == 2:
        b = GoodsInfo.objects.filter(gtype=2)
        return render(request,'list.html',{'b':b,'a':a})
    elif int(a) == 3:
        b = GoodsInfo.objects.filter(gtype=3)
        return render(request,'list.html',{'b':b,'a':a})

    elif int(a) == 4:
        b = GoodsInfo.objects.filter(gtype=4)
        return render(request,'list.html',{'b':b,'a':a})

    elif int(a) == 5:
        b = GoodsInfo.objects.filter(gtype=5)
        return render(request,'list.html',{'b':b,'a':a})

    elif int(a) == 6:
        b = GoodsInfo.objects.filter(gtype=6)
        return render(request,'list.html',{'b':b,'a':a})

def price(request,a):
    if int(a) == 1:
        b = GoodsInfo.objects.filter(gtype=1).order_by('-gprice')

        return render(request,'list.html',{'b':b,'a':a})
    elif int(a) == 2:
        b = GoodsInfo.objects.filter(gtype=2).order_by('-gprice')
        return render(request,'list.html',{'b':b,'a':a})
    elif int(a) == 3:
        b = GoodsInfo.objects.filter(gtype=3).order_by('-gprice')
        return render(request,'list.html',{'b':b,'a':a})

    elif int(a) == 4:
        b = GoodsInfo.objects.filter(gtype=4).order_by('-gprice')
        return render(request,'list.html',{'b':b,'a':a})

    elif int(a) == 5:
        b = GoodsInfo.objects.filter(gtype=5).order_by('-gprice')
        return render(request,'list.html',{'b':b,'a':a})

    elif int(a) == 6:
        b = GoodsInfo.objects.filter(gtype=6).order_by('-gprice')
        return render(request,'list.html',{'b':b,'a':a})


