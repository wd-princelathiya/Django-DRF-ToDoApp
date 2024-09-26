from django.contrib import admin
from .models import User


class UserAdminConfig(admin.ModelAdmin):
    model = User
    search_fields = ("email",)
    list_filter = ("email",)
    ordering = ("-created_date",)
    list_display = ("email",)


admin.site.register(User, UserAdminConfig)
