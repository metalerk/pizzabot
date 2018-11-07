from django.urls import reverse

from rest_framework.test import APITestCase

from ordering.models import (
	Pizza,
	Customer,
)


class TestOrderingCase(APITestCase):
	def setUp(self):
		self.pizza = Pizza.objects.create(name='Pepperoni')
		self.customer = Customer.objects.create(
			first_name='Luis Esteban',
			last_name='Rodriguez',
		)

	def test_create_order(self):
		data = {
			'pizza': self.pizza.id,
			'customer': self.customer.id,
			'size': 30,
			'customer_address': '22 Jump Street, NY',
		}
		response = self.client.post(
			reverse('ordering:order-list1'),
			data
		)
		self.assertTrue(response.data['created'])

		data['size'] = 29
		response = self.client.post(
			reverse('ordering:order-list1'),
			data,
			content_type='application/json'
		)
		self.assertFalse(response.data['created'])

		data['size'] = 51
		response = self.client.post(
			reverse('ordering:order-list1'),
			data,
			content_type='application/json'
		)
		self.assertFalse(response.data['created'])

	
	def test_update_order(self):
		data = {
			'pizza': self.pizza.id,
			'customer': self.customer.id,
			'size': 35,
			'customer_address': '21 Jump Street, NY',
		}
		response = self.client.post(
			reverse('ordering:order-list1'),
			data
		)
		self.assertTrue(response.data['created'])

		order = response.data['data']
		data['size'] = 45
		response = self.client.put(
			reverse('ordering:order-detail-update', kwargs={'order_id': order['id']}),
			data
		)
		self.assertTrue(response.data['updated'])


	def test_remove_order(self):
		data = {
			'pizza': self.pizza.id,
			'customer': self.customer.id,
			'size': 50,
			'customer_address': '21 Jump Street, NY',
		}
		response = self.client.post(
			reverse('ordering:order-list1'),
			data
		)
		self.assertTrue(response.data['created'])
		order = response.data['data']
		response = self.client.delete(
			reverse('ordering:order-detail-delete', kwargs={'order_id': order['id']}),
			data
		)
		self.assertTrue(response.data['deleted'])


	def test_get_client_orders(self):
		data = {
			'pizza': self.pizza.id,
			'customer': self.customer.id,
			'size': 50,
			'customer_address': '21 Jump Street, NY',
		}
		response = self.client.get(
			reverse('ordering:order-detail-customer', kwargs={'customer_id': self.customer.id}),
			data
		)
		self.assertEqual(response.data['data'], [])
		response = self.client.post(
			reverse('ordering:order-list1'),
			data
		)
		self.assertTrue(response.data['created'])
		response = self.client.get(
			reverse('ordering:order-detail-customer', kwargs={'customer_id': self.customer.id}),
			data
		)
		self.assertNotEqual(response.data['data'], [])
