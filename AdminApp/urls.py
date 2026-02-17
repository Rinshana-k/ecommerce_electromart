from django.urls import path
from AdminApp import views

urlpatterns=[
    path('dashboard/',views.dashboard,name="dashboard"),
    path('add_categories/',views.add_categories,name="add_categories"),
    path('display_categories/',views.display_categories,name="display_categories"),
    path('save_categories/',views.save_categories,name="save_categories"),
    path('edit_category/<int:c_id>/',views.edit_category,name="edit_category"),
    path('update_category/<int:c_id>/',views.update_category,name="update_category"),
    path('delete_category/<int:c_id>/',views.delete_category,name="delete_category"),

    path('add_products/',views.add_products,name="add_products"),
    path('save_products/',views.save_products,name="save_products"),
    path('display_products/',views.display_products,name="display_products"),
    path('edit_product/<int:p_id>/',views.edit_product,name="edit_product"),
    path('update_product/<int:p_id>/',views.update_product,name="update_product"),
    path('delete_product/<int:p_id>/',views.delete_product,name="delete_product"),

    path('',views.admin_login_page,name="admin_login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('contact_details/',views.contact_details,name="contact_details"),
    path('delete_contact_details/<int:c_id>/',views.delete_contact_details,name="delete_contact_details"),
    path('order_details/',views.order_details,name="order_details"),
    path('cart_details/',views.cart_details,name="cart_details"),


]