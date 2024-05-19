from django.urls import path
from pg1 import views

urlpatterns=[
path('',views.reg,name="reg"),
path('/login',views.login,name="login"),
path('insert',views.insertData,name="insertData"),
path('user_login',views.user_login,name="user_login"),
path('/home',views.home,name="home"),
path('logout/', views.user_logout, name="user_logout"),
]
