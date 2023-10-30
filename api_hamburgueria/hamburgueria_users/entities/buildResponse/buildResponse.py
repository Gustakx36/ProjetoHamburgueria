from drf_yasg.utils import swagger_auto_schema
from django.http import HttpResponse, JsonResponse
import json

def selectSimplesResponse(Objeto):
    try:
        result = Objeto.selectSimples()
        if result['response'] and len(result['object']) != 0:
            return JsonResponse(result['object'], status=200, json_dumps_params={'ensure_ascii': False}, safe=False)
        return JsonResponse({'response' : result['text']}, status=204, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        return JsonResponse({'response' : e}, status=500, json_dumps_params={'ensure_ascii': False})

def selectSimplesAtvInatvResponse(Objeto, ativo):
    try:
        result = Objeto.selectSimples(ativo)
        if result['response'] and len(result['object']) != 0:
            return JsonResponse(result['object'], status=200, json_dumps_params={'ensure_ascii': False}, safe=False)
        return JsonResponse({'response' : result['text']}, status=204, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        return JsonResponse({'response' : e}, status=500, json_dumps_params={'ensure_ascii': False})

def selectSimplesPorIdResponse(Objeto, id):
    try:
        result = Objeto.selectSimplesPorId(id)
        if result['response']:
            return JsonResponse(result['object'], status=200, json_dumps_params={'ensure_ascii': False}, safe=False)
        return JsonResponse({'response' : result['text']}, status=204, json_dumps_params={'ensure_ascii': False})
    except:
        return JsonResponse({'response' : 'Erro ao conectar com o banco!'}, status=500, json_dumps_params={'ensure_ascii': False})

def insertSimplesResponse(Objeto, params):
    try:
        result = Objeto.insertSimples(params)
        if result['response']:
            return JsonResponse({'response' : result['text']}, status=202, json_dumps_params={'ensure_ascii': False})
        return JsonResponse({'response' : result['text']}, status=422, json_dumps_params={'ensure_ascii': False})
    except:
        return JsonResponse({'response' : 'Erro ao conectar com o banco!'}, status=500, json_dumps_params={'ensure_ascii': False})

def updateSimplesResponse(Objeto, params, id):
    try:
        exist = Objeto.selectSimplesPorId(id)
        if not exist['response']:
            return JsonResponse({'response' : f"{Objeto.string.capitalize()} não existe"}, status=204, json_dumps_params={'ensure_ascii': False})
        result = Objeto.updateSimples(params, id)
        if result['response']:
            return JsonResponse({'response' : result['text']}, status=202, json_dumps_params={'ensure_ascii': False})
        return JsonResponse({'response' : result['text']}, status=422, json_dumps_params={'ensure_ascii': False})
    except:
        return JsonResponse({'response' : 'Erro ao conectar com o banco!'}, status=500, json_dumps_params={'ensure_ascii': False})

def deleteSimplesResponse(Objeto, id):
    try:
        exist = Objeto.selectSimplesPorId(id)
        if not exist['response']:
            return JsonResponse({'response' : f"{Objeto.string.capitalize()} não existe"}, status=204, json_dumps_params={'ensure_ascii': False})
        result = Objeto.deleteSimples(id)
        if result['response']:
            return JsonResponse({'response' : result['text']}, status=202, json_dumps_params={'ensure_ascii': False})
        return JsonResponse({'response' : result['text']}, status=422, json_dumps_params={'ensure_ascii': False})
    except:
        return JsonResponse({'response' : 'Erro ao conectar com o banco!'}, status=500, json_dumps_params={'ensure_ascii': False})

# --- Fuções extras ---

def selectSimplesOrderItemResponse(Objeto, id_pedido):
    try:
        result = Objeto.selectSimples(id_pedido)
        if result['response']:
            return JsonResponse(result['object'], status=200, json_dumps_params={'ensure_ascii': False}, safe=False)
        return JsonResponse({'response' : result['text']}, status=204, json_dumps_params={'ensure_ascii': False})
    except:
        return JsonResponse({'response' : 'Erro ao conectar com o banco!'}, status=500, json_dumps_params={'ensure_ascii': False})

def verificaLoginExistenteResponse(Objeto, params):
    try:
        result = Objeto.verificaLoginExistente(params)
        if result['response']:
            return JsonResponse(result['object'], status=200, json_dumps_params={'ensure_ascii': False}, safe=False)
        return JsonResponse({}, status=204, json_dumps_params={'ensure_ascii': False})
    except:
        return JsonResponse({'response' : 'Erro ao conectar com o banco!'}, status=500, json_dumps_params={'ensure_ascii': False})