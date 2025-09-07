from django.urls import path
from .views import *
from . import views

app_name = "account"
urlpatterns = [
    path("", home_view, name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", loginView.as_view(), name="login"),
    path('logout/',views.logout_view,name='logout')
]