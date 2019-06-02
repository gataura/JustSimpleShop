from django.contrib import admin

# Register your models here.
from cart.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['userName', 'address', 'order']


admin.site.register(Order, OrderAdmin)
