from django.contrib import admin

# Register your models here.
from orderbook.models import ShopCart, Order, OrderProduct

admin.site.register(ShopCart)
admin.site.register(Order)
admin.site.register(OrderProduct)