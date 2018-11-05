from rest_framework import serializers

from ordering.models import (
	Pizza,
	Customer,
	Order,
)


class PizzaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pizza
		fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
	pizza = serializers.SerializerMethodField()
	customer = serializers.SerializerMethodField()


	def get_pizza(self, obj):
		return obj.pizza.id

	def get_customer(self, obj):
		return obj.customer.get_fullname


	class Meta:
		model = Order
		fields = '__all__'
