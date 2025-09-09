from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Fields", {"fields": ("phone_number", "address" , "account_type")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra Fields", {"fields": ("phone_number", "address","account_type" )}),
    )

    list_display = ("username", "email", "phone_number", "account_type","address", "is_staff")

admin.site.register(MyUser, MyUserAdmin)