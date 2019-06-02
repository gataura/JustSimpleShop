from django.contrib import admin
from .models import Category, Product
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


class MyUserAdmin(UserAdmin):
    # override the default sort column
    ordering = ('date_joined',)
    # if you want the date they joined or other columns displayed in the list,
    # override list_display too
    list_display = ('username', 'email', 'date_joined', 'first_name', 'last_name', 'is_staff')


# finally replace the default UserAdmin with yours
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

admin.site.register(Product, ProductAdmin)
