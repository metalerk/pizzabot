from django.urls import re_path, path

import ordering.views as views


app_name = 'ordering'

order_list = views.OrderViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

order_detail = views.OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

order_customer_detail = views.OrderViewSet.as_view({
    'get': 'get_customer_orders',
})

urlpatterns = [
    path('', order_list, name='order-list1'),
    path('<int:page>/', order_list, name='order-list2'),
    path('<int:page>/<int:items>/', order_list, name='order-list3'),
    path('<uuid:order_id>/', order_detail, name='order-detail-retrieve'),
    path('<uuid:order_id>/', order_detail, name='order-detail-update'),
    path('<uuid:order_id>/', order_detail, name='order-detail-delete'),
    path('customer/<uuid:customer_id>/', order_customer_detail, name='order-detail-customer'),
    path('customer/<uuid:customer_id>/<int:page>/', order_customer_detail, name='order-detail-customer2'),
    path('customer/<uuid:customer_id>/<int:page>/<int:items>/', order_customer_detail, name='order-detail-customer3'),
]
