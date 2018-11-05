from django.core.paginator import Paginator

from rest_framework import viewsets
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
	serializer_class = OrderSerializer

	def list(self, request, page=1):
		page = request.data.pop('page', page)
		paginator = Paginator(self.queryset.all(), 5)
		orders = paginator.get_page(page)
		if paginator.num_pages < int(page) or int(page) <= 0:
			return Response({})
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
			return Response({'data': serializer.data})
		
		except Exception as e:
			return Response({
				'error': str(e),
			})


	def retrieve(self, request, pk=None):
		pass


	def update(self, request, pk=None):
		pass


	def destroy(self, request, pk=None):
		pass
