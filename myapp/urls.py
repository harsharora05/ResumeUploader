from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
 path('', views.home, name='home'),
 path('upload/', views.upload, name='upload'),
 path('signup', views.handleSignUp, name="handleSignUp"),
 path('login', views.handeLogin, name="handleLogin"),
 path('logout', views.handelLogout, name="handleLogout")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)