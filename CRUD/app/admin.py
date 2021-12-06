from django.contrib import admin
from .models import(
    User
)

# Register your models here.
@admin.register(User)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['Email','Username']
