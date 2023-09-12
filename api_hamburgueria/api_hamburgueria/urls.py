from hamburgueria_users import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.vazio),
    re_path(r'^orders?(/)$', views.order),
    re_path(r'orders/(?P<int>[0-9]+)?(\/)$', views.orderInt),
    re_path(r'^logins?(/)$', views.login),
    re_path(r'logins/(?P<int>[0-9]+)?(\/)$', views.loginInt),
    re_path(r'^type?(/)$', views.type),
    re_path(r'type/(?P<int>[0-9]+)?(\/)$', views.typeInt),
    re_path(r'^product?(/)$', views.products),
    re_path(r'product/(?P<int>[0-9]+)?(\/)$', views.productsInt),
    re_path(r'orderItem/(?P<int>[0-9]+)?(\/)$', views.orderItem),
    re_path(r'orderUnique/(?P<int>[0-9]+)?(\/)$', views.orderItemInt),
]
