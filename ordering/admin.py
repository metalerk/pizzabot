from django.contrib import admin

from ordering.models import (
	Pizza,
	Customer,
	Order,
)


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
	list_display = ('id', 'name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'address')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'pizza', 'size', 'customer', 'customer_address', 'timestamp', 'updated')
