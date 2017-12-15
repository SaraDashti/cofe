from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'jewcofe'

urlpatterns = [
    path('signup/', views.usersignup),
    path('login/', views.userlogin,),
    path('logout/', views.userlogout),
]
