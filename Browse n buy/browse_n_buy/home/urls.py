"""browse_n_buy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

    path('',views.home,name="apphome"),
    path('about/',views.about,name="appabout"),
    path('cart/',views.cart_view,name="cart"),
    path('search', views.search_view,name='search'),
    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),


    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='home/customer_login.html'),name='customerlogin'),
    path('logout', LogoutView.as_view(template_name='home/logout.html'),name='logout'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('contact_us',views.cutomer_contact_us),
    path('myprofile', views.my_profile_view,name='my-profile'),
    path('order', views.customer_address_view),
    path('paymentsuccess', views.payment_success_view,name='payment-success'),
    path('my-order', views.my_order_view,name='my-order'),
    path("make-payment",views.razorpay_test)


]
