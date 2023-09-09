from hamburgueria_users.connection import connection as conn
from hamburgueria_users.normalize import normaliza as norm
from hamburgueria_users.entities import order_items

class Order:
    def __init__(self):
        self.table = 'orders'
        self.primaryKey = 'id'
        self.listOptionsInsertIgnore = ['id', 'finalizado', 'data_hora', 'nome_cliente']
        self.listOptionsUpdateIgnore = ['id', 'finalizado', 'data_hora', 'nome_cliente']
        self.string = 'pedido'

    def selectSimples(self):
        sql = f"""
            SELECT * FROM
                {self.table}
        """
        result = conn.read_query(sql)
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
            'text' : f"{self.string.capitalize()}s não foi encontrado!",
            'object' : result
        }

    def insertSimples(self, params):
        sql = f"""
            INSERT INTO {self.table}
                ()
            VALUES
                ()
        """
        resultOrder = conn.execute_query(sql, [])
        pedido = self.selectSimplesPorIdPedidoNovo()
        if resultOrder:
            result = norm.normalizeInsertOrder(params, ['observacao', 'preco', 'id_produto', 'id_pedido'], pedido)
            for item in result:
                order_items.insertSimples(item)
        return {
            'response' : resultOrder,
            'text' : pedido
        }

    def updateSimples(self, params, id):
        paramsNormalize = norm.normalizeParamsUpdate(params, self.selectColunas(), self.listOptionsInsertIgnore)
        if not paramsNormalize['response']:
            return {
                'response' : False,
                'text' : paramsNormalize['error']
            }
        paramsNormalize['params'].append(id)
        sql = f"UPDATE {self.table} SET {paramsNormalize['values']} WHERE id = %s"
        result = conn.execute_query(sql, paramsNormalize['params'])
        if not result:
            return {
                'response' : result,
                'text' : f"Erro ao inserir o {self.string}!"
            }
        return {
            'response' : result,
            'text' : f"{self.string.capitalize()} foi alterado com sucesso!"
        }

    def deleteSimples(self, id):
        sql = f"DELETE FROM {self.table} WHERE id = %s"
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

    # --- Fuções extras ---

    def selectSimplesPorIdPedidoNovo(self):
            sql = f"""
                SELECT id, data_hora FROM
                    {self.table}
                WHERE
                    nome_cliente IS NULL
                AND
                    finalizado = 0
                ORDER BY id 
                    DESC 
                LIMIT 1;
            """
            result = conn.read_query_bind(sql, [], True)
            return result