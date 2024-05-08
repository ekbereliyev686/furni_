from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('shop',views.shop,name='shop'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('thankyou',views.thankyou,name='thankyou'),
    path('test',views.test,name='test'),

    path('content',views.content,name='content'),

]


