from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . import productService as pro
# Create your views here.

def index(request):
    template = loader.get_template('loginPage.html')
    appTitle = 'Site Title'
    listCity = ["İstanbul","Ankara","İzmir","Antalya"]
    context = {        
         'appTitle': appTitle,
         'listCity' : listCity
        }
        
    return HttpResponse(template.render(context,request))

#user login function
def userLogin(request):
    email = request.POST['email']
    password = request.POST['password']
    if (email =='ali@alimail.com' and password=='12345'):
         return HttpResponseRedirect(reverse('dashboard'))
        
    else:
        print('Giriş Başarısız')
    print(email,password)
    return HttpResponseRedirect(reverse('index'))


# open dashboard
def dashboard(request):
    template = loader.get_template('dashboard.html')
    context = { 'productList' : pro.productList() 
               }
    print(pro.productList())
    return HttpResponse(template.render(context,request))


def addrecord(request):
    
    if 'title' in request.POST:
        title = request.POST['title']
    else:
        title = False
    
    if 'detail' in request.POST:
        detail = request.POST['detail']
    else:
        detail = False
    
    if 'price' in request.POST:
        price= request.POST['price']
    else:
        price = False
        
    pro.productSave(title=title,detail=detail,price=price)

    return HttpResponseRedirect(reverse('index'))
  

  
  
     
  



    
