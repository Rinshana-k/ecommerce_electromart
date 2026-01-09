from django.shortcuts import render,redirect
from unicodedata import category

from AdminApp.models import CategoryDb,ProductDb
from WebApp.models import *
# Create your views here.

def Home_page(request):
    categories=CategoryDb.objects.all()
    return render(request,"Home.html",{'categories':categories})

def About_page(request):
    categories=CategoryDb.objects.all()
    return render(request,"About.html",{'categories':categories})

def Contact_page(request):
    categories=CategoryDb.objects.all()
    return render(request,"Contact.html",{'categories':categories})

def All_products(request):
    products=ProductDb.objects.all()
    categories=CategoryDb.objects.all()
    return render(request,"All_products.html",{'products':products,'categories':categories})

def filtered_product(request,cat_name):
    categories = CategoryDb.objects.all()
    products=ProductDb.objects.filter(CategoryName=cat_name)
    return render(request,"filtered_products.html",{'products':products,'categories':categories})

def single_product(request,pro_id):
    product=ProductDb.objects.get(id=pro_id)
    categories=CategoryDb.objects.all()
    return render(request,"single_product.html",{'product':product,'categories':categories})

def signin_signup(request):
    return render(request,"signin_signup.html")

def save_Registration(request):
    if request.method=="POST":
        u_name=request.POST.get("u_name")
        password=request.POST.get("pswd")
        confirm_password=request.POST.get("c_pswd")
        email=request.POST.get("email")
        if UserRegistrationDb.objects.filter(UserName=u_name).exists():
        #     User already exists
           return redirect(signin_signup)
        elif UserRegistrationDb.objects.filter(Email=email).exists():
        #     email already exists
            return redirect(signin_signup)
        else:
            obj=UserRegistrationDb(UserName=u_name,Password=password,ConfirmPassword=confirm_password,Email=email)
            obj.save()
        return redirect(signin_signup)

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if UserRegistrationDb.objects.filter(UserName=username,Password=password).exists():
            request.session['UserName']=username
            request.session['Password']=password
            return redirect(Home_page)
        else:
            return redirect(signin_signup)
    else:
        return redirect(signin_signup)

def user_logout(request):
     del request.session['UserName']
     del request.session['Password']
     return redirect(Home_page)

def save_contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        Phone=request.POST.get("mob")
        subject=request.POST.get("sub")
        mesasage=request.POST.get("msg")
        obj=ContactDb(Name=name,Email=email,Phone=Phone,Subject=subject,Message=mesasage)
        obj.save()
        return redirect(Contact_page)

def help(request):
    categories=CategoryDb.objects.all()
    return render(request,"help.html",{'categories':categories})

def support(request):
    categories=CategoryDb.objects.all()
    return render(request,"support.html",{'categories':categories})

def cart(request):
    categories = CategoryDb.objects.all()
    return render(request,"cart.html",{'categories':categories})


def checkout(request):
    categories = CategoryDb.objects.all()
    return render(request,"checkout.html",{'categories':categories})
