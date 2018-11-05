from rest_framework import serializers

from ordering.models import (
	Pizza,
	Customer,
	Order,
)


class PizzaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pizza
		fields = (
			'id',
			'name',
		)


class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = (
			'id',
			'address',
		)


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = (
			'id',
			'pizza__id',
			'size',
			'customer_address',
			'timestamp',
			'updated',
		)
