from django.shortcuts import render
from zzh.models import Biao
from zzh.models import Uname1
list = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
ddaan = 1
wname = 2

def update(request):
     gtitle = request.POST['xiugai']
     htitle = request.POST['xiugaih']
     gnei = request.POST['xiugai1']
     object1 = Biao.objects.filter(title=gtitle)
     print(object1)
     if object1 == []:
          return render(request, '没有.html')
     else:
          obj = Biao.objects.get(title=gtitle)
          obj.title = htitle
          obj.nei = gnei
          obj.save()
          return index(request)


def index(request):
    articles = Biao.objects.all()
    return render(request, 'article.html', {'articles_List': articles})
def index1(request):
      return render(request, '登录.html')
def wangye(request):
     return render(request,'注册.html')
def dl(request):
     booklist = Uname1.objects.values_list('yonghu','mima')
     uname = request.POST['uname']
     upwd = request.POST['upwd']
     print(booklist)
     for i in booklist:
          list.append(i[0])
          list1.append(i[1])
     if uname in list:
          sy = list.index(uname)
          if upwd == list1[int(sy)]:
               return index(request)
          else:
               return render(request, '密碼錯誤.html')
     else:
          return render(request, '賬號錯誤.html')

def zhuce(request):
     namelist = Uname1.objects.values_list('yonghu')
     zcname = request.POST['zcname']
     name = request.POST['name']
     zcmima = request.POST['zcmima']
     quemima = request.POST['quemima']
     wenti = request.POST['wenti']
     daan = request.POST['daan']
     print(namelist)
     for i in namelist:
          list2.append(i[0])
     if zcname in list2:
          return render(request,'存在.html')
     else:
          if zcmima == quemima:
               Uname1.objects.create(yonghu=zcname,mima=zcmima,name=name,qmima=quemima,wenti=wenti,daan=daan)
               return render(request, '登录.html')
          else:
               return render(request,'两次输入密码不一致.html')



def article_page(request, article_id):
    article = Biao.objects.get(pk=article_id)
    return render(request, '内容.html', {'article': article})

def fabiao(request):
     return render(request,'发表新.html')
def xin(request):
     ztitle = request.POST['xintitle']
     znei = request.POST['xinneirong']
     Biao.objects.create(title=ztitle,nei=znei)
     return index(request)

def xiu(request):
     return render(request,'修改.html')

def wang(request):
     return render(request,'忘记密码.html')

def wangji(request):
     global wname
     wname = request.POST['uname']
     print(wname)
     object2 = Uname1.objects.get(yonghu=wname)
     print(object2)
     if object2 == []:
          return render(request, '賬號錯誤.html')
     else:
          global ddaan
          wwenti = object2.wenti
          ddaan = object2.daan
          return render(request,'输入答案.html',{'wwenti':wwenti})



def pddn(request):
     uiyu= request.POST['srdn']
     if uiyu == ddaan:
          return render(request,'忘记改密码.html')
     else:
          return render(request,'密碼錯誤.html')
def wjgmm(request):
     a = request.POST['xmm']
     b = request.POST['xmm1']
     print(a)
     obj = Uname1.objects.get(yonghu=wname)
     if a == b:

          obj.mima = a
          obj.save()
     else:
          return render(request,'两次输入密码不一致.html')


def search(request):
     p = request.POST['search']
     if not p:
          return render(request,'没有.html')
     else:
          post_list = Biao.objects.values_list('title','nei').filter(title=p)
          print(post_list)
          a = post_list[0][0]
          b = post_list[0][1]
          return render(request,'搜索显示.html',{'a':a,'b':b})

def shanchu(request):
     return render(request,'删除博客.html')

def delete(request):
     a = request.POST['delete']
