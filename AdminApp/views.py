from platform import uname

from django.shortcuts import render,redirect
from AdminApp.models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import *
from django.contrib import messages
# Create your views here.

def dashboard(request):
    category=CategoryDb.objects.count()
    product=ProductDb.objects.count()
    return render(request,"dashboard.html",{'category':category,'product':product})

def add_categories(request):
    return render(request,"Add_categories.html")

def display_categories(request):
    category=CategoryDb.objects.all()
    return render(request,"display_categories.html",{'category':category})

def save_categories(request):
    if request.method=="POST":
        C_name=request.POST.get("c_name")
        description=request.POST.get("despn")
        C_img=request.FILES['c_img']
        obj=CategoryDb(Category_name=C_name,Description=description,Category_img=C_img)
        obj.save()
        messages.success(request,"Category saved successfully....")
        return redirect(add_categories)

def edit_category(request,c_id):
    category=CategoryDb.objects.get(id=c_id)
    return render(request,"edit_category.html",{'category':category})

def update_category(request,c_id):
    C_name = request.POST.get("c_name")
    description = request.POST.get("despn")
    try:
        C_img=request.FILES['c_img']
        fs=FileSystemStorage()
        file=fs.save(C_img.name,C_img)
    except MultiValueDictKeyError:
        file=CategoryDb.objects.get(id=c_id).Category_img
    CategoryDb.objects.filter(id=c_id).update(Category_name=C_name,Description=description,Category_img=file)
    return redirect(display_categories)

def delete_category(request,c_id):
    data=CategoryDb.objects.filter(id=c_id)
    data.delete()
    return redirect(display_categories)

def add_products(request):
    categories=CategoryDb.objects.all()
    return render(request,"Add_products.html",{'categories':categories})

def save_products(request):
    if request.method=="POST":
        category_name=request.POST.get("c_name")
        product_name=request.POST.get("p_name")
        price=request.POST.get("price")
        short_description=request.POST.get("s_description")
        detailed_description=request.POST.get("d_description")
        brand=request.POST.get("brand")
        p_img1=request.FILES['p_img1']
        p_img2=request.FILES['p_img2']
        p_img3=request.FILES['p_img3']
        obj=ProductDb(CategoryName=category_name,ProductName=product_name,Price=price,Short_Description=short_description,Detailed_Description=detailed_description,
                      Brand=brand,Product_Image1=p_img1,Product_Image2=p_img2,Product_Image3=p_img3)
        obj.save()
        messages.success(request,"product saved successfully....")
        return redirect(add_products)

def display_products(request):
    categories=ProductDb.objects.all()
    return render(request,"display_products.html",{'categories':categories})

def edit_product(request,p_id):
    categories=CategoryDb.objects.all()
    product=ProductDb.objects.get(id=p_id)
    return render(request,"Edit-product.html",{'product':product,'categories':categories})

def update_product(request,p_id):
    if request.method=="POST":
        category_name = request.POST.get("c_name")
        product_name = request.POST.get("p_name")
        price = request.POST.get("price")
        short_description = request.POST.get("s_description")
        detailed_description = request.POST.get("d_description")
        brand = request.POST.get("brand")
        try:
            p_img1 = request.FILES['p_img1']
            fs=FileSystemStorage()
            file1=fs.save(p_img1.name,p_img1)
        except MultiValueDictKeyError:
            file1=ProductDb.objects.get(id=p_id).Product_Image1

        try:
            p_img2=request.FILES['p_img2']
            fs=FileSystemStorage()
            file2=fs.save(p_img2.name,p_img2)
        except MultiValueDictKeyError:
            file2=ProductDb.objects.get(id=p_id).Product_Image2

        try:
            p_img3=request.FILES['p_img3']
            fs=FileSystemStorage()
            file3=fs.save(p_img3.name,p_img3)
        except MultiValueDictKeyError:
            file3=ProductDb.objects.get(id=p_id).Product_Image3

        ProductDb.objects.filter(id=p_id).update(CategoryName=category_name,ProductName=product_name,Price=price,Short_Description=short_description,Detailed_Description=detailed_description,
                      Brand=brand,Product_Image1=file1,Product_Image2=file2,Product_Image3=file3)
        return redirect(display_products)

def delete_product(request,p_id):
    data=ProductDb.objects.filter(id=p_id)
    data.delete()
    return redirect(display_products)


def admin_login_page(request):
    return render(request,"Admin_login_page.html")
def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pswd=request.POST.get("password")
        if User.objects.filter(username__contains=uname).exists():
            data=authenticate(username=uname,password=pswd)
            if data is not None:
                login(request,data)
                request.session['username']=uname
                request.session['password']=pswd
                messages.success(request,"Welcome to ElectroMart Admin dashboard ")
                return redirect(dashboard)
            else:
                messages.error(request,"Invalid Password")
                return redirect(admin_login_page)

        else:
            messages.warning(request,"Username Doesnot exist...")
            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

def contact_details(request):
    contact=ContactDb.objects.all()
    return render(request,"contact_details.html",{'contact':contact})

def delete_contact_details(request,c_id):
    data=ContactDb.objects.get(id=c_id)
    data.delete()
    return redirect(contact_details)

def order_details(request):
    orders=CheckoutDb.objects.all()
    return render(request,"order_details.html",{'orders':orders})

def cart_details(request):
    cart_detail=CartDb.objects.all()
    return render(request,"cart_details.html",{'cart_detail':cart_detail})
