from hamburgueria_users import views
from django.urls import path

urlpatterns = [
    path('', views.vazio),
    path('orders', views.order),
    path('orders/<int>', views.orderInt),
    path('logins', views.login),
    path('logins/<int>', views.loginInt),
    path('type', views.type),
    path('type/<int>', views.typeInt),
    path('product', views.products),
    path('product/<int>', views.productsInt),
    path('item', views.orderItem),
    path('item/<int>', views.orderItemInt),
]
