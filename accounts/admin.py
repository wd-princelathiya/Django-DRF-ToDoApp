from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ("email",)
    list_filter = ("email",)
    ordering = ("-created_date",)
    list_display = ("email",)
    


admin.site.register(User, UserAdminConfig)
