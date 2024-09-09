from django.urls import path, include
from . import views
from .views import register

urlpatterns = [
 
    path('register/', register, name='register'),

]