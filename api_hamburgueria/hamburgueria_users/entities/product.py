from hamburgueria_users.connection import connection as conn
from hamburgueria_users.normalize import normaliza as norm

class Product:
    def __init__(self):
        self.table = 'product'
        self.primaryKey = 'id'
        self.listOptionsInsertIgnore = ['id']
        self.listOptionsUpdateIgnore = ['id']
        self.string = 'produto'

    def selectSimples(self, ativo):
        ativoString = "%s"
        if ativo != None:
            ativoString = "ativo = %s"
        else:
            ativo = 1
        sql = f"""
            SELECT * FROM
                {self.table}
            WHERE
                {ativoString}
        """
        result = conn.read_query_bind(sql, [ativo], False)
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

    def insertSimples(self, params):
        paramsNormalize = norm.normalizeParamsInsert(params, self.selectColunas(), self.listOptionsInsertIgnore)
        if not paramsNormalize['response']:
            return {
                'response' : False,
                'text' : paramsNormalize['error']
            }
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