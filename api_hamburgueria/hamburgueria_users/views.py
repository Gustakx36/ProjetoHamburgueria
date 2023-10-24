from hamburgueria_users.normalize.normaliza import normalizeDecodeParams as norm
from .entities import orders, logins, type_product, product, order_items
from .entities.buildResponse import buildResponse as bRes
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .entities_params import *
from .status_code import *

requestJson = {}

def vazio(request):
    return JsonResponse({'response' : 'Projeto Unip Alunos : (Gustavo, Julio, Wellington)'})

@csrf_exempt
@swagger_auto_schema(methods=['get'], responses=statusGet('pedido'))
@swagger_auto_schema(methods=['post'], manual_parameters=paramsOrders(), responses=statusPost('pedido'))
@api_view(['GET', 'POST'])
def order(request):
    Object = orders.Order()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
        if norm(request.body) == {}:
            requestJson['pedidos'] = norm(requestJson['pedidos'])
        return bRes.insertSimplesResponse(Object, requestJson)

@csrf_exempt
@swagger_auto_schema(methods=['get'], responses=statusGetInt('pedido'))
@swagger_auto_schema(methods=['put'], manual_parameters=paramsOrdersId(), responses=statusPut('pedido'))
@swagger_auto_schema(methods=['delete'], responses=statusDelete('pedido'))
@api_view(['GET', 'PUT', 'DELETE'])
def orderInt(request, id):
    Object = orders.Order()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, id)
    if request.method == 'PUT':
        requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
        return bRes.updateSimplesResponse(Object, requestJson, id)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, id)

@csrf_exempt
@swagger_auto_schema(methods=['get'], responses=statusGet('login'))
@swagger_auto_schema(methods=['post'], manual_parameters=paramsLogins(), responses=statusPost('login'))
@api_view(['GET', 'POST'])
def login(request):
    Object = logins.Login()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
        return bRes.insertSimplesResponse(Object, requestJson)

@csrf_exempt
@swagger_auto_schema(methods=['get'], responses=statusGetInt('login'))
@swagger_auto_schema(methods=['put'], manual_parameters=paramsLoginsId(), responses=statusPut('login'))
@swagger_auto_schema(methods=['delete'], responses=statusDelete('login'))
@api_view(['GET', 'PUT', 'DELETE'])
def loginInt(request, id):
    Object = logins.Login()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, id)
    if request.method == 'PUT':
        requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
        return bRes.updateSimplesResponse(Object, requestJson, id)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, id)

@csrf_exempt
@swagger_auto_schema(methods=['get'], responses=statusGet('tipo'))
@swagger_auto_schema(methods=['post'], manual_parameters=paramsType(), responses=statusPost('tipo'))
@api_view(['GET', 'POST'])
def type(request):
    Object = type_product.Type()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
        return bRes.insertSimplesResponse(Object, requestJson)

@csrf_exempt
@swagger_auto_schema(methods=['get'], responses=statusGetInt('tipo'))
@swagger_auto_schema(methods=['put'], manual_parameters=paramsTypeId(), responses=statusPut('tipo'))
@swagger_auto_schema(methods=['delete'], responses=statusDelete('tipo'))
@api_view(['GET', 'PUT', 'DELETE'])
def typeInt(request, id):
    Object = type_product.Type()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, id)
    if request.method == 'PUT':
        requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
        return bRes.updateSimplesResponse(Object, requestJson, id)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, id)

@csrf_exempt
@swagger_auto_schema(methods=['get'], responses=statusGet('produto'))
@swagger_auto_schema(methods=['post'], manual_parameters=paramsProduct(), responses=statusPost('produto'))
@api_view(['GET', 'POST'])
def products(request):
    Object = product.Product()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
        return bRes.insertSimplesResponse(Object, requestJson)

@csrf_exempt
@swagger_auto_schema(methods=['get'], responses=statusGetInt('produto'))
@swagger_auto_schema(methods=['put'], manual_parameters=paramsProductId(), responses=statusPut('produto'))
@swagger_auto_schema(methods=['delete'], responses=statusDelete('produto'))
@api_view(['GET', 'PUT', 'DELETE'])
def productsInt(request, id):
    Object = product.Product()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, id)
    if request.method == 'PUT':
        requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
        return bRes.updateSimplesResponse(Object, requestJson, id)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, id)
    
@csrf_exempt
@swagger_auto_schema(methods=['get'], responses=statusGet('item'))
@api_view(['GET'])
def orderItem(request, id):
    Object = order_items.Order_items()
    if request.method == 'GET':
        return bRes.selectSimplesOrderItemResponse(Object, id)

@csrf_exempt
@swagger_auto_schema(methods=['get'], responses=statusGetInt('item'))
@api_view(['GET'])
def orderItemInt(request, id):
    Object = order_items.Order_items()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, id)

@csrf_exempt
@swagger_auto_schema(methods=['post'], manual_parameters=paramsVerificaLogin(), responses=statusGetInt('login'))
@api_view(['POST'])
def loginVerify(request):
    Object = logins.Login()
    if request.method == 'POST':
        requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
        return bRes.verificaLoginExistenteResponse(Object, requestJson)