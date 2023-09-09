from .entities.buildResponse import buildResponse as bRes
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .entities import orders, logins, type_product, product, order_items

def vazio(request):
    return JsonResponse({'api_hamburgueria' : 'Projeto Unip Alunos : (Gustavo, Julio, Wellington)'})

@csrf_exempt
def order(request):
    metodo = {
        'GET' : request.GET,
        'POST' : request.POST,
        'DELETE' : ''
    }[request.method]
    Object = orders.Order()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.getlist('pedidos[]'))
        return bRes.insertSimplesResponse(Object, metodo.getlist('pedidos[]'))
    return bRes.methodNotExist()

@csrf_exempt
def orderInt(request, int):
    Object = orders.Order()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, int)
    if request.method == 'POST':
        return bRes.updateSimplesResponse(Object, request.POST.dict(), int)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, int)

@csrf_exempt
def login(request):
    metodo = {
        'GET' : request.GET,
        'POST' : request.POST,
        'DELETE' : ''
    }[request.method]
    Object = logins.Login()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        print('a')
        print(metodo.dict())
        print('b')
        print(int)
        return bRes.insertSimplesResponse(Object, metodo.dict())
    return bRes.methodNotExist()

@csrf_exempt
def loginInt(request, int):
    Object = logins.Login()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, int)
    if request.method == 'POST':
        return bRes.updateSimplesResponse(Object, request.POST.dict(), int)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, int)

@csrf_exempt
def type(request):
    metodo = {
        'GET' : request.GET,
        'POST' : request.POST,
        'DELETE' : ''
    }[request.method]
    Object = type_product.Type()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        return bRes.insertSimplesResponse(Object, metodo.dict())
    return bRes.methodNotExist()

@csrf_exempt
def typeInt(request, int):
    Object = type_product.Type()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, int)
    if request.method == 'POST':
        return bRes.updateSimplesResponse(Object, request.POST.dict(), int)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, int)

@csrf_exempt
def products(request):
    metodo = {
        'GET' : request.GET,
        'POST' : request.POST,
        'DELETE' : ''
    }[request.method]
    Object = product.Product()
    if request.method == 'GET':
        return bRes.selectSimplesResponse(Object)
    if request.method == 'POST':
        return bRes.insertSimplesResponse(Object, metodo.dict())
    return bRes.methodNotExist()

@csrf_exempt
def productsInt(request, int):
    Object = product.Product()
    if request.method == 'GET':
        return bRes.selectSimplesPorIdResponse(Object, int)
    if request.method == 'POST':
        return bRes.updateSimplesResponse(Object, request.POST.dict(), int)
    if request.method == 'DELETE':
        return bRes.deleteSimplesResponse(Object, int)
