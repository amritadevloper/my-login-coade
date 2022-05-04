from email import message
from django.shortcuts import redirect, render
from .models import Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def project(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['your_email']
        password=request.POST['password']
        comfirm_password=request.POST['comfirm_password']
        if User.objects.filter(username=uname).exists():
            messages.info(request,"username allready exists")
            return redirect("/")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email allready exists")
            return redirect("/")
        elif password!=comfirm_password:
            messages.info(request,"password missmatch")
            return redirect("/")
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
            user.save()
            messages.success(request,"signup successfully")
            return render(request,'login.html')
    else:
        return render(request,'index.html')
def login(request):
    if request.method=='POST':
        
        uname=request.POST['username']  
        password=request.POST['pass']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'product.html') 
        else:
            messages.info(request,"invalied username or password")
            return render(request,'login.html')
            
    else: 
       return render(request,'login.html')
def product(request):
    if request.method=='POST':
        p=Product()
        p.name=request.POST['name']
        p.price=request.POST['price']
        p.category=request.POST['cato']
        p.company=request.POST['comp']
        p.save()
        messages.success(request,"Add Product Successfully")
        return render(request,'product.html')
    else:  
        messages.success(request,"Not Product Added")  
        return render(request,'product.html')
def show(request):
    p=Product.objects.all()
    return render(request,'show.html',{'data':p})   
def deldata(request):
    id=request.GET['id']
    Product.objects.filter(id=id).delete()
    p=Product.objects.all()
    return render(request,'show.html',{'data':p}) 
def updatdata(request):
         #id=request.GET['id']
        #pro=Product.objects.get(id=id)
        if request.method=='POST':
         p=Product()
         p.id=request.POST['id']
         p.name=request.POST['name']
         p.price=request.POST['price']
         p.category=request.POST['cato']
         p.company=request.POST['comp']
         p.save()
         p=Product.objects.all()
         messages.success(request,"Update Product Successfully")
         return render(request,'show.html',{'data':p})
        else:  
         messages.success(request,"Not Updated Product")  
         return render(request,'show.html')

def updatdatashow(request):
        id=request.GET['id']
        pro=Product.objects.get(id=id)
        return render(request,'update.html',{'data':pro})
def search(request):
    search=request.POST['search'] 
    p=Product.objects.filter(name=search).all()
    return render(request,'show.html',{'data':p})    
   