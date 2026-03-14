
from django.shortcuts import render,redirect
from unicodedata import category
from django.contrib import messages
from AdminApp.models import CategoryDb,ProductDb
from WebApp.models import *
import razorpay
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
    latest_products=ProductDb.objects.order_by('-id')[:3]
    return render(request,"All_products.html",{'products':products,
                                               'categories':categories,
                                               'latest_products':latest_products})

def filtered_product(request,cat_name):
    categories = CategoryDb.objects.all()
    products=ProductDb.objects.filter(CategoryName=cat_name)
    return render(request,"filtered_products.html",{'products':products,
                                                    'categories':categories
                                                    })

def single_product(request,pro_id):
    product=ProductDb.objects.get(id=pro_id)
    categories=CategoryDb.objects.all()
    return render(request,"single_product.html",{'product':product,
                                                 'categories':categories
                                                 })

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

def save_to_cart(request):
    if request.method=="POST":
        u_name=request.POST.get("username")
        product_name=request.POST.get("product_name")
        price=request.POST.get("price")
        qty=request.POST.get("qty")
        total_price=request.POST.get("t_price")
        obj=CartDb(username=u_name,product_name=product_name,price=price,quantity=qty,total_price=total_price)
        obj.save()
        messages.success(request, " Item Add successfully ")
        return redirect(cart)

def cart(request):
    products=CartDb.objects.filter(username=request.session['UserName'])
    categories = CategoryDb.objects.all()

    sub_total=0
    shipping_charge=0
    total=0

    for i in products:
        sub_total+=i.total_price

        if sub_total>100000:
            shipping_charge=0
        elif sub_total>50000:
            shipping_charge=100
        else:
            shipping_charge=200

        total=sub_total+shipping_charge

    return render(request,"cart.html",{'categories':categories,'products':products,
                                       'sub_total':sub_total,
                                       'shipping_charge':shipping_charge,
                                       'total':total})

def cart_delete(request,id):
    data=CartDb.objects.get(id=id)
    data.delete()
    return redirect(cart)

def checkout(request):
    categories = CategoryDb.objects.all()
    products=CartDb.objects.filter(username=request.session['UserName'])
    sub_total = 0
    shipping_charge = 0
    total = 0

    for i in products:
        sub_total += i.total_price

        if sub_total > 100000:
            shipping_charge = 0
        elif sub_total > 50000:
            shipping_charge = 100
        else:
            shipping_charge = 200

        total = sub_total + shipping_charge
    return render(request,"checkout.html",{'categories':categories,
                                           'products':products,
                                           'sub_total': sub_total,
                                           'shipping_charge': shipping_charge,
                                           'total': total})

def save_to_checkout(request):
    if request.method=="POST":
        f_name=request.POST.get("f_name")
        email=request.POST.get("email")
        mob=request.POST.get("mobile")
        place=request.POST.get("place")
        address=request.POST.get("addrs")
        pincode=request.POST.get("pin")
        msg=request.POST.get("message")
        total_amount=request.POST.get("t_amount")
        username=request.POST.get("u_name")
        obj=CheckoutDb(fullname=f_name,email=email,mobile=mob,place=place,address=address,pincode=pincode,message=msg,
                       total_amount=total_amount,username=username)
        obj.save()
        return redirect(payments)

def payments(request):
    customer=CheckoutDb.objects.order_by("-id").first()

    pay=customer.total_amount
    amount=int(pay*100)
    pay_str=str(amount)

    if request.method=="POST":
        order_currency="INR"
        client=razorpay.Client(auth=('rzp_test_0ib0jPwwZ7I1lT','VjHNO5zKeKxz8PYe7VnzwxMR'))
        payment=client.order.Create({
            'amount':amount,
            'currency':order_currency,
        })

    return render(request,"payments.html",{
        'pay_str':pay_str,
        'amount':amount,

    })
