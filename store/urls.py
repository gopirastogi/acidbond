from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
 
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('blog/', views.blog, name='blog'),
    path('orders/', views.orders, name='orders'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('base/', views.base, name='base'),
    path('mail/', views.mail, name='mail'),
    path('shop_now/', views.shop_now, name='shop_now'),
    path('order/<uuid:order_id>/', views.checkout, name='checkout'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('profile/', views.customer_profile, name='customer_profile'),
    path('create/', views.customer_create, name='customer_create'),
    path('update/', views.customer_update, name='customer_update'),
    

]