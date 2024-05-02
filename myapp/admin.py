from django.contrib import admin
from .models import userreg
# Register your models here.

@admin.register(userreg)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id' , 'username' , 'email' , 'password' ]