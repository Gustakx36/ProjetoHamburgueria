from django.urls import path, re_path
from hamburgueria_users import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Hamburgueria",
      default_version='v1',
      description="API Para projeto de uma lanchonete (UNIP)",
      terms_of_service="https://www.app.com/policies/terms/",
      contact=openapi.Contact(email="gustavobruno12333@gmail.com"),
      license=openapi.License(name="API Hamburgueria"),
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.vazio),
    re_path(r'^orders/?$', views.order),
    re_path(r'^orders/(?P<id>[0-9]+)/?$', views.orderInt),
    re_path(r'^logins/?$', views.login),
    re_path(r'^logins/(?P<id>[0-9]+)/?$', views.loginInt),
    re_path(r'^type/?$', views.type),
    re_path(r'^type/(?P<id>[0-9]+)/?$', views.typeInt),
    re_path(r'^product/?$', views.products),
    re_path(r'^product/(?P<id>[0-9]+)/?$', views.productsInt),
    re_path(r'^orderItem/(?P<id>[0-9]+)/?$', views.orderItem),
    re_path(r'^orderUnique/(?P<id>[0-9]+)/?$', views.orderItemInt),
    re_path(r'^verifyLogin/?$', views.loginVerify),
    re_path(r'^schemapi/?$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/?$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
