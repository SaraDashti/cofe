from django.conf.urls import url
from . import views

urlpatterns = [
    path('signup/', views.usersignup, name="signup"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),
]
