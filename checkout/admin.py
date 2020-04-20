from django.contrib import admin

from .models import Order, OrderLineItem

"""register order and orderadmin to the admin panel"""
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)
