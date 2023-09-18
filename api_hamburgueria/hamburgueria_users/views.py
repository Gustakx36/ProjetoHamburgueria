from hamburgueria_users.normalize.normaliza import normalizeDecodeParams as norm
from .entities import orders, logins, type_product, product, order_items
from .entities.buildResponse import buildResponse as bRes
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from .entities_params import *

requestJson = {}

def vazio(request):
    return JsonResponse({'response' : 'Projeto Unip Alunos : (Gustavo, Julio, Wellington)'})

@csrf_exempt
@swagger_auto_schema(methods=['post'], manual_parameters=paramsOrders())
@api_view(['GET', 'POST'])
def order(request):
    Object = orders.Order()
    requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        if norm(request.body) == {}:
            requestJson['pedidos'] = norm(requestJson['pedidos'])
        return bRes.insertSimplesResponse(Object, requestJson)
    return bRes.methodNotExist()

@csrf_exempt
@swagger_auto_schema(methods=['put'], manual_parameters=paramsOrdersId())
@api_view(['GET', 'PUT', 'DELETE'])
def orderInt(request, id):
    Object = orders.Order()
    requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, id)
    if request.method == 'PUT':
        if norm(request.body) == {}:
            requestJson['ativo'] = 1 if requestJson['ativo'] == 'true' else 0
        return bRes.updateSimplesResponse(Object, requestJson, id)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, id)
    return bRes.methodNotExist()

@csrf_exempt
@swagger_auto_schema(methods=['post'], manual_parameters=paramsLogins())
@api_view(['GET', 'POST'])
def login(request):
    Object = logins.Login()
    requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        return bRes.insertSimplesResponse(Object, requestJson)
    return bRes.methodNotExist()

@csrf_exempt
@swagger_auto_schema(methods=['put'], manual_parameters=paramsLoginsId())
@api_view(['GET', 'PUT', 'DELETE'])
def loginInt(request, id):
    Object = logins.Login()
    requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
    print(requestJson)
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, id)
    if request.method == 'PUT':
        if norm(request.body) == {}:
            requestJson['ativo'] = 1 if requestJson['ativo'] == 'true' else 0
        return bRes.updateSimplesResponse(Object, requestJson, id)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, id)
    return bRes.methodNotExist()

@csrf_exempt
@swagger_auto_schema(methods=['post'], manual_parameters=paramsType())
@api_view(['GET', 'POST'])
def type(request):
    Object = type_product.Type()
    requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        return bRes.insertSimplesResponse(Object, requestJson)
    return bRes.methodNotExist()

@csrf_exempt
@swagger_auto_schema(methods=['put'], manual_parameters=paramsTypeId())
@api_view(['GET', 'PUT', 'DELETE'])
def typeInt(request, id):
    Object = type_product.Type()
    requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, id)
    if request.method == 'PUT':
        return bRes.updateSimplesResponse(Object, requestJson, id)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, id)
    return bRes.methodNotExist()

@csrf_exempt
@swagger_auto_schema(methods=['post'], manual_parameters=paramsProduct())
@api_view(['GET', 'POST'])
def products(request):
    Object = product.Product()
    requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        return bRes.insertSimplesResponse(Object, requestJson)
    return bRes.methodNotExist()

@csrf_exempt
@swagger_auto_schema(methods=['put'], manual_parameters=paramsProductId())
@api_view(['GET', 'PUT', 'DELETE'])
def productsInt(request, id):
    Object = product.Product()
    requestJson = norm(request.body) if norm(request.body) != {} else request.GET.dict()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, id)
    if request.method == 'PUT':
        return bRes.updateSimplesResponse(Object, requestJson, id)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, id)
    return bRes.methodNotExist()
    
@csrf_exempt
@api_view(['GET'])
def orderItem(request, id):
    Object = order_items.Order_items()
    if request.method == 'GET':
        return bRes.selectSimplesOrderItemResponse(Object, id)
    return bRes.methodNotExist()

@csrf_exempt
@api_view(['GET'])
def orderItemInt(request, id):
    Object = order_items.Order_items()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, id)
    return bRes.methodNotExist()
