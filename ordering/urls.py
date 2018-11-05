from django.urls import re_path, path

import ordering.views as views


app_name = 'ordering'

order_list = views.OrderViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    path('', order_list, name='order-list'),
    re_path(r'(?P<page>[-\w]+)$', order_list, name='order-list-page'),
    path('', order_list, name='order-list-create'),
]
