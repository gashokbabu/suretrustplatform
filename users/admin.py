from django.contrib import admin
from .models import User
# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     fields=('email','first_name','last_name','password','is_active','is_staff','is_superuser','groups','user_permissions','last_login','date_joined')
admin.site.register(User)