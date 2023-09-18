from drf_yasg import openapi

def paramsOrders():
    nome_cliente = openapi.Parameter(
        'nome_cliente', 
        openapi.IN_QUERY, 
        description="Nome do cliente", 
        type=openapi.TYPE_STRING, 
        required=True)

    pedidos = openapi.Parameter(
        'pedidos', 
        openapi.IN_QUERY, 
        description="Pedidos do cliente", 
        type=openapi.TYPE_ARRAY, 
        items=openapi.Items(
            type=openapi.TYPE_OBJECT, 
            required=['id_produto', 'observacao'],
            properties=paramsPedidos()),
        required=True)
    params = [nome_cliente, pedidos]
    return params

def paramsPedidos():
    return {
        'id_produto': openapi.Schema(type=openapi.TYPE_INTEGER),
        'observacao': openapi.Schema(type=openapi.TYPE_STRING)
    }

def paramsOrdersId():
    finalizado = openapi.Parameter(
        'finalizado', 
        openapi.IN_QUERY, 
        description="Status do pedido", 
        type=openapi.TYPE_BOOLEAN)

    nome_cliente = openapi.Parameter(
        'nome_cliente', 
        openapi.IN_QUERY, 
        description="Nome do cliente", 
        type=openapi.TYPE_STRING)
    params = [finalizado, nome_cliente]
    return params

def paramsLogins():
    nome = openapi.Parameter(
        'nome', 
        openapi.IN_QUERY, 
        description="Nome do usuário", 
        type=openapi.TYPE_STRING, 
        required=True)

    login = openapi.Parameter(
        'login', 
        openapi.IN_QUERY, 
        description="Login do usuário", 
        type=openapi.TYPE_STRING, 
        required=True)

    senha = openapi.Parameter(
        'senha', 
        openapi.IN_QUERY, 
        description="Senha do usuário", 
        type=openapi.TYPE_STRING, 
        required=True)
    params = [nome, login, senha]
    return params

def paramsLoginsId():
    nome = openapi.Parameter(
        'nome', 
        openapi.IN_QUERY, 
        description="Nome do usuário", 
        type=openapi.TYPE_STRING)

    login = openapi.Parameter(
        'login', 
        openapi.IN_QUERY, 
        description="Login do usuário", 
        type=openapi.TYPE_STRING)

    ativo = openapi.Parameter(
        'ativo', 
        openapi.IN_QUERY, 
        description="Status do usuário", 
        type=openapi.TYPE_BOOLEAN)
    params = [nome, login, ativo]
    return params

def paramsType():
    descricao = openapi.Parameter(
        'descricao', 
        openapi.IN_QUERY, 
        description="Descrição do tipo", 
        type=openapi.TYPE_STRING, 
        required=True)

    params = [descricao]
    return params

def paramsTypeId():
    descricao = openapi.Parameter(
        'descricao', 
        openapi.IN_QUERY, 
        description="Descrição do tipo", 
        type=openapi.TYPE_STRING)

    params = [descricao]
    return params

def paramsProduct():
    nome = openapi.Parameter(
        'nome', 
        openapi.IN_QUERY, 
        description="Nome do produto", 
        type=openapi.TYPE_STRING, 
        required=True)
    
    descricao = openapi.Parameter(
        'descricao', 
        openapi.IN_QUERY, 
        description="Descrição do tipo", 
        type=openapi.TYPE_STRING, 
        required=True)
    
    tipo_produto = openapi.Parameter(
        'tipo_produto', 
        openapi.IN_QUERY, 
        description="Descrição do tipo", 
        type=openapi.TYPE_STRING, 
        required=True)
    
    imagem = openapi.Parameter(
        'imagem', 
        openapi.IN_QUERY, 
        description="Descrição do tipo", 
        type=openapi.TYPE_STRING, 
        required=True)
    
    preco = openapi.Parameter(
        'preco', 
        openapi.IN_QUERY, 
        description="Descrição do tipo", 
        type=openapi.TYPE_STRING, 
        required=True)

    params = [nome, descricao, tipo_produto, imagem, preco]
    return params

def paramsProductId():
    nome = openapi.Parameter(
        'nome', 
        openapi.IN_QUERY, 
        description="Nome do produto", 
        type=openapi.TYPE_STRING)
    
    descricao = openapi.Parameter(
        'descricao', 
        openapi.IN_QUERY, 
        description="Descrição do produto", 
        type=openapi.TYPE_STRING)
    
    tipo_produto = openapi.Parameter(
        'tipo_produto', 
        openapi.IN_QUERY, 
        description="Tipo do produto", 
        type=openapi.TYPE_INTEGER)
    
    imagem = openapi.Parameter(
        'imagem', 
        openapi.IN_QUERY, 
        description="Link de imagem do produto", 
        type=openapi.TYPE_STRING)
    
    preco = openapi.Parameter(
        'preco', 
        openapi.IN_QUERY, 
        description="Preço do produto", 
        type=openapi.TYPE_NUMBER)

    params = [nome, descricao, tipo_produto, imagem, preco]
    return params