import json
from json import JSONDecodeError

def normalizeParamsInsert(params, columns, options=[]):
    listParams = []
    listColumns = []
    listFails = []
    fail = False
    for keys in columns:
        if keys in options:
            continue
        if not keys in params:
            fail = True
            listFails.append(keys)
            continue
        listParams.append(params[keys])
        listColumns.append(keys)
    if fail:
        return {
            'response' : False,
            'error' : f"Faltam os seguintes parametros ({', '.join(listFails)})"
        }
    return {
        'response' : True,
        'params' : listParams,
        'columns' : ', '.join(listColumns),
        'values' : ', '.join(list(map(lambda x:"%s", listColumns)))
    }

def normalizeParamsUpdate(params, columns, options=[]):
    listParams = []
    listColumns = []
    listFails = []
    fail = False
    for keys in columns:
        if keys in options:
            continue
        if not keys in params:
            fail = True
            listFails.append(keys)
            continue
        listParams.append(params[keys])
        listColumns.append(keys)
    if fail:
        return {
            'response' : False,
            'error' : f"Faltam os seguintes parametros ({', '.join(listFails)})"
        }
    return {
        'response' : True,
        'params' : listParams,
        'values' : ', '.join(list(map(lambda x:f"{x} = %s", listColumns)))
    } 

def normalizeInsertOrder(params, columns, pedido):
    listaProdutos = params['pedidos']
    listaDeParams = []
    for item in listaProdutos:
        item['id_pedido'] = pedido
        result = normalizeParamsInsert(item, columns)
        if not result['response']:
            return result
        listaDeParams.append(result)
    return {
        'response' : True,
        'params' : listaDeParams
    }

def normalizeParamsOrder(params, itens):
    listFails = []
    fail = False
    for keys in itens:
        print(keys)
        if not keys in params:
            print(itens)
            fail = True
            listFails.append(keys)
            continue
    if fail:
        return {
            'response' : False,
            'error' : f"Faltam os seguintes parametros ({', '.join(listFails)})"
        }
    return {
        'response' : True
    }

def decodeParams(paramString):
    try:
        return json.loads(paramString)
    except JSONDecodeError:
        return {}
