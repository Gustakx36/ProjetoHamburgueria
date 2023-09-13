from django.http import JsonResponse

def selectSimplesResponse(Objeto):
    result = Objeto.selectSimples()
    if result['response']:
        return JsonResponse({
            'object' : result['object']
        }, status=200, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'response' : result['text']}, status=204, json_dumps_params={'ensure_ascii': False})

def selectSimplesPorIdResponse(Objeto, id):
    result = Objeto.selectSimplesPorId(id)
    if result['response']:
        return JsonResponse({
            'object' : result['object']
        }, status=200, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'response' : result['text']}, status=204, json_dumps_params={'ensure_ascii': False})

def insertSimplesResponse(Objeto, params):
    result = Objeto.insertSimples(params)
    if result['response']:
        return JsonResponse({'response' : result['text']}, status=202, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'response' : result['text']}, status=422, json_dumps_params={'ensure_ascii': False})

def updateSimplesResponse(Objeto, params, id):
    exist = Objeto.selectSimplesPorId(id)
    if exist == None:
        return JsonResponse({'response' : f"{Objeto.string.capitalize()} não existe"}, status=204, json_dumps_params={'ensure_ascii': False})
    result = Objeto.updateSimples(params, id)
    if result['response']:
        return JsonResponse({'response' : result['text']}, status=202, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'response' : result['text']}, status=422, json_dumps_params={'ensure_ascii': False})

def deleteSimplesResponse(Objeto, id):
    exist = Objeto.selectSimplesPorId(id)
    if exist == None:
        return JsonResponse({'response' : f"{Objeto.string.capitalize()} não existe"}, status=204, json_dumps_params={'ensure_ascii': False})
    result = Objeto.deleteSimples(id)
    if result['response']:
        return JsonResponse({'response' : result['text']}, status=202, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'response' : result['text']}, status=422, json_dumps_params={'ensure_ascii': False})

def methodNotExist():
    return JsonResponse({'response' : "Metodo não existe para esse EndPoint"}, status=405, json_dumps_params={'ensure_ascii': False})

# --- Fuções extras ---

def selectSimplesOrderItemResponse(Objeto, id_pedido):
    result = Objeto.selectSimples(id_pedido)
    if result['response']:
        return JsonResponse({
            'object' : result['object']
        }, status=200, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'response' : result['text']}, status=204, json_dumps_params={'ensure_ascii': False})

