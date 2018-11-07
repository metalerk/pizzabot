from django.core.paginator import Paginator

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ordering.models import (
	Pizza,
	Customer,
	Order,
)
from ordering.serializers import (
	PizzaSerializer,
	CustomerSerializer,
	OrderSerializer,
)
from utils import get_or_none


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects

	def list(self, request, page=1, items=5):
		page = request.data.pop('page', page)	
		paginator = Paginator(self.queryset.all(), items)
		orders = paginator.get_page(page)
		if paginator.num_pages < int(page) or int(page) <= 0:
			return Response({'data': []})
		serializer = OrderSerializer(orders, many=True)
		return Response({
			'data': serializer.data,
			'page': page,
			'num_pages': paginator.num_pages,
		})


	def create(self, request):
		try:
			pizza_obj = get_or_none(
				Pizza,
				id=request.data.get('pizza', None)
			)
			customer_obj = get_or_none(
				Customer,
				id=request.data.get('customer', None)
			)
			size = int(request.data.get('size'))
			if size < 30 or size > 50:
				raise Exception('Invalid size. Must be beetwen 30 and 50 cms.')
			data = dict()
			data.update({
				'pizza': pizza_obj,
				'customer': customer_obj,
				'size': size,
				'customer_address': request.data.get('customer_address', ''),
			})
			order = self.queryset.create(**data)
			serializer = OrderSerializer(order)	
			return Response({'data': serializer.data, 'created': True,})
		
		except Exception as e:
			return Response({
				'error': str(e),
				'created': False,
			})


	def retrieve(self, request, order_id=None):
		order = get_or_none(
			Order,
			id=order_id
		)
		if order is None:
			return Response({'error': 'Order does not exist.'})
		serializer = OrderSerializer(order)
		return Response({
			'data': serializer.data
		})


	def update(self, request, order_id=None):
		order = get_or_none(
			Order,
			id=order_id
		)
		if order is None:
			return Response({
				'error': 'Order does not exist.',
				'updated': False
			})

		data = dict()
		data = request.data.dict()
		pizza_obj = get_or_none(
			Pizza,
			id=request.data.get('pizza', None)
		)
		customer_obj = get_or_none(
			Customer,
			id=request.data.get('customer', None)
		)
		if pizza_obj is not None:
			data.update({'pizza': pizza_obj})

		if customer_obj is not None:
			data.update({'customer': customer_obj})

		try:
			order = self.queryset.filter(id=order_id).update(**data)
			return Response({
				'updated': True if order is not None else False
			})
		except Exception as e:
			return Response({
				'error': str(e),
				'updated': False,
			})


	def destroy(self, request, order_id=None):
		order = get_or_none(
			Order,
			id=order_id
		)
		if order is None:
			return Response({
				'error': 'Order does not exist.',
				'deleted': False
			})

		try:
			order.delete()
			return Response({
				'deleted': True,
			})
		except Exception as e:
			return Response({
				'error': str(e),
			})

	@action(detail=True, methods=['get'])
	def get_customer_orders(self, request, customer_id, page=1, items=5):
		page = request.data.pop('page', page)	
		paginator = Paginator(self.queryset.filter(customer=customer_id), items)
		orders = paginator.get_page(page)
		if paginator.num_pages < int(page) or int(page) <= 0:
			return Response({'data': []})
		serializer = OrderSerializer(orders, many=True)
		return Response({
			'data': serializer.data,
			'page': page,
			'num_pages': paginator.num_pages,
		})

