from hamburgueria_users.connection import connection as conn

class Order_items:
    def __init__(self):
        self.table = 'order_items'
        self.primaryKey = 'id'
        self.listOptionsInsertIgnore = ['id']
        self.listOptionsUpdateIgnore = ['id']
        self.string = 'item'

    def selectSimples(self, id_pedido):
        sql = f"""
            SELECT oi.*, p.preco, p.descricao, p.nome FROM
                {self.table} oi
            WHERE
                id_pedido = %s
            INNER JOIN 
                product p
            ON p.id = oi.id_produto
        """
        result = conn.read_query_bind(sql, [id_pedido], False)
        return {
            'response' : not result == None,
            'text' : f"{self.string.capitalize()}s não foram encontrados!",
            'object' : result
        }

    def selectSimplesPorId(self, id):
        sql = f"""
            SELECT * FROM
                {self.table}
            WHERE
                id = %s
        """
        result = conn.read_query_bind(sql, [id], True)
        return {
            'response' : not result == None,
            'text' : f"{self.string.capitalize()} não foi encontrado!",
            'object' : result
        }

    def insertSimples(self, paramsNormalize):
        sql = f"""
            INSERT INTO {self.table}
                ({paramsNormalize['columns']})
            VALUES
                ({paramsNormalize['values']})"""
        result = conn.execute_query(sql, paramsNormalize['params'])
        if not result:
            return {
                'response' : result,
                'text' : f"Erro ao inserir o {self.string}!"
            }
        return {
            'response' : result,
            'text' : f"{self.string.capitalize()} foi inserido com sucesso!"
        }

    def deleteSimples(self, id):
        sql = f"DELETE FROM {self.table} WHERE id_pedido = %s"
        result = conn.execute_query(sql, [id])
        if not result:
            return {
                'response' : False,
                'text' : f"Erro ao deletar o {self.string}"
            }
        return {
            'response' : result,
            'text' : f"{self.string.capitalize()} foi deletado com sucesso!"
        }

    def selectColunas(self):
        sql = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'Gustakx36$hamburgueria' AND TABLE_NAME = '{self.table}';"
        result = list(map(lambda x:x['COLUMN_NAME'], conn.read_query(sql)))
        return result