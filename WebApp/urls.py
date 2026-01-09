from django.urls import path
from WebApp import views
urlpatterns=[
    path('',views.Home_page,name="Home"),
    path('About/',views.About_page,name="About"),
    path('Contact/',views.Contact_page,name="Contact"),
    path('All_products/',views.All_products,name="All_products"),
    path('filtered_product/<cat_name>/',views.filtered_product,name="filtered_product"),
    path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
    path('new_user/',views.signin_signup,name="signin_signup"),
    path('save_Registration/',views.save_Registration,name="save_Registration"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('help/',views.help,name="help"),
    path('support/',views.support,name="support"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),

]