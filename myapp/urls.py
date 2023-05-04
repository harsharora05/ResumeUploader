from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
 path('', views.home, name='home'),
 path('upload/', views.upload, name='upload'),
 path('signup', views.handleSignUp, name="handleSignUp"),
 path('login', views.handeLogin, name="handleLogin"),
 path('logout', views.handelLogout, name="handleLogout")
]