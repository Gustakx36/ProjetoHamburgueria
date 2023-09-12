from .entities import orders, logins, type_product, product, order_items
from hamburgueria_users.normalize.normaliza import decodeParams as norm
from .entities.buildResponse import buildResponse as bRes
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

requestJson = {}

def vazio(request):
    return JsonResponse({'response' : 'Projeto Unip Alunos : (Gustavo, Julio, Wellington)'})

@csrf_exempt
def order(request):
    Object = orders.Order()
    requestJson = norm(request.body)
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        return bRes.insertSimplesResponse(Object, requestJson)
    return bRes.methodNotExist()

@csrf_exempt
def orderInt(request, int):
    Object = orders.Order()
    requestJson = norm(request.body)
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, int)
    if request.method == 'POST':
        return bRes.updateSimplesResponse(Object, requestJson, int)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, int)
    return bRes.methodNotExist()

@csrf_exempt
def login(request):
    Object = logins.Login()
    requestJson = norm(request.body)
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        return bRes.insertSimplesResponse(Object, requestJson)
    return bRes.methodNotExist()

@csrf_exempt
def loginInt(request, int):
    Object = logins.Login()
    requestJson = norm(request.body)
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, int)
    if request.method == 'POST':
        return bRes.updateSimplesResponse(Object, requestJson, int)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, int)
    return bRes.methodNotExist()

@csrf_exempt
def type(request):
    Object = type_product.Type()
    requestJson = norm(request.body)
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        return bRes.insertSimplesResponse(Object, requestJson)
    return bRes.methodNotExist()

@csrf_exempt
def typeInt(request, int):
    Object = type_product.Type()
    requestJson = norm(request.body)
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, int)
    if request.method == 'POST':
        return bRes.updateSimplesResponse(Object, requestJson, int)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, int)
    return bRes.methodNotExist()

@csrf_exempt
def products(request):
    Object = product.Product()
    requestJson = norm(request.body)
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        return bRes.insertSimplesResponse(Object, requestJson)
    return bRes.methodNotExist()

@csrf_exempt
def productsInt(request, int):
    Object = product.Product()
    requestJson = norm(request.body)
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, int)
    if request.method == 'POST':
        return bRes.updateSimplesResponse(Object, requestJson, int)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, int)
    return bRes.methodNotExist()
    
@csrf_exempt
def orderItem(request, int):
    Object = order_items.Order_items()
    if request.method == 'GET':
        return bRes.selectSimplesOrderItemResponse(Object, int)
    return bRes.methodNotExist()

@csrf_exempt
def orderItemInt(request, int):
    Object = order_items.Order_items()
    requestJson = norm(request.body)
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, int)
    if request.method == 'POST':
        return bRes.updateSimplesResponse(Object, requestJson, int)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, int)
    return bRes.methodNotExist()
