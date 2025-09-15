from django.urls import path
from .views import *
from . import views

from django.contrib.auth import views as auth_views

app_name = "account"
urlpatterns = [
    # Home
    path("", home_view, name="home"),
    
    # User Authentication
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", loginView.as_view(), name="login"),
    path('logout/',views.logout_view,name='logout'),

    # User Profile
    path('profile/<int:pk>/',profile.as_view(),name='profile'),
    path('profile/change/<int:pk>',Updateprofile.as_view(),name='Update_profile'),
    
    # Password change
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    # Password reset
    path('reset_password/', MyPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]