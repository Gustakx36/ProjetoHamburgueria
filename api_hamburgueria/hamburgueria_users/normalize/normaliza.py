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
    listaProdutos = params.getlist('pedidos[]')
    if listaProdutos == 0:
        return {
            'response' : True,
            'text' : f"Faltam os seguintes parametros (pedidos)"
        }
    for item in listaProdutos:
        print(json.loads(item))