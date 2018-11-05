from rest_framework import viewsets

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


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def list(self, request, page=1):
		pass


	def create(self, request):
		pass


	def retrieve(self, request, pk=None):
		pass


	def update(self, request, pk=None):
		pass


	def destroy(self, request, pk=None):
		pass
