from json import JSONDecodeError
import json

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
    listValid = []
    for keys in columns:
        if keys in options:
            continue 
        listValid.append(keys)
    for keys in params:
        if keys in options:
            continue
        if not keys in columns:
            listValid.append(keys)
            continue
        listParams.append(params[keys])
        listColumns.append(keys)
    if len(listParams) == 0:
        return {
            'response' : False,
            'error' : f"Parametros validos ({', '.join(listValid)})"
        }
    return {
        'response' : True,
        'params' : listParams,
        'values' : ', '.join(list(map(lambda x:f"{x} = %s", listColumns)))
    } 

def normalizeInsertOrder(params, columns, pedido, options=[]):
    listaProdutos = params['pedidos']
    listaDeParams = []
    for item in listaProdutos:
        item['id_pedido'] = pedido
        result = normalizeParamsInsert(item, columns, options)
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
        if not keys in params:
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

def normalizaExistenciaProdutos(params):
    listaProdutos = []
    for item in params['pedidos']:
        listaProdutos.append(item['id_produto'])
    return listaProdutos


def normalizeDecodeParams(paramString):
    try:
        return json.loads(paramString)
    except JSONDecodeError:
        return {}
