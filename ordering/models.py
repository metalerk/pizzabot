from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from uuid import uuid4


class Pizza(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid4,
		editable=False
	)
	name = models.CharField(max_length=150, blank=False, null=False)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'pizza'
		verbose_name_plural = 'Pizzas'
		ordering = ['-name']


class Customer(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid4,
		editable=False
	)
	name = models.CharField(max_length=150, blank=False, null=False)
	address = models.TextField()

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'customer'
		verbose_name_plural = 'Customers'
		ordering = ['-name']


class Order(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid4,
		editable=False
	)
	pizza = models.ForeignKey(
		Pizza,
		on_delete=models.CASCADE,
		related_name='pizza_order'
	)
	size = models.PositiveIntegerField(
		validators=[MaxValueValidator(50), MinValueValidator(30)]
	)
	customer = models.ForeignKey(
		Customer,
		on_delete=models.CASCADE,
		related_name='customer_order'
	)
	customer_address = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.id.__str__()

	class Meta:
		db_table = 'order'
		verbose_name_plural = 'Orders'
		ordering = ['-updated']
