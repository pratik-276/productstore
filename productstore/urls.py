from django.contrib import admin
from django.urls import path
from productuser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.authpage),
    path('login', views.login),
    path('signup', views.signup)
]
