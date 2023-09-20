def statusGet(string):
    return {
        200 : statusDefault_200_(string, False), 
        204 : statusDefault_204_(string),
        500 : statusDefault_500_()
    }

def statusGetInt(string):
    return {
        200 : statusDefault_200_(string, True),
        204 : statusDefault_204_(string),
        500 : statusDefault_500_()
    }

def statusPost(string):
    return {
        202 : statusDefault_202_(string, 'inserido'), 
        422 : statusDefaul_422_(string, 'inserir'),
        500 : statusDefault_500_()
    }

def statusPut(string):
    return {
        202 : statusDefault_202_(string, 'atualizado'), 
        204 : statusDefault_204_(string),  
        422 : statusDefaul_422_(string, 'atualizar'),
        500 : statusDefault_500_()
    }

def statusDelete(string):
    return {
        202 : statusDefault_202_(string, 'deletado'), 
        204 : statusDefault_204_(string),  
        422 : statusDefaul_422_(string, 'deletar'),
        500 : statusDefault_500_()
    }

def statusDefault_200_(string, onlyOne):
    stringMore = '' if onlyOne else 's'
    return f'{string.capitalize()}{stringMore} encontrado{stringMore}!'

def statusDefault_204_(string):
    return f'Nenhum {string} encontrado!'

def statusDefault_202_(string, operacao):
    return f'{string.capitalize()} {operacao}!'

def statusDefaul_422_(string, operacao):
    return f'Erro ao {operacao} o {string}!'

def statusDefault_500_():
    return 'Erro ao conectar com o banco!'