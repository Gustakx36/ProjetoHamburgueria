from hamburgueria_users.connection import connection as conn
from hamburgueria_users.normalize import normaliza as norm

class Login:
    def __init__(self):
        self.table = 'logins'
        self.primaryKey = 'id'
        self.listOptionsInsertIgnore = ['id', 'ativo', 'senha']
        self.listOptionsUpdateIgnore = ['id', 'senha']
        self.string = 'login'

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
            'text' : f"{self.string.capitalize()} não foi encontrado!",
            'object' : result
        }

    def insertSimples(self, params):
        if not 'senha' in params:
            return {
                'response' : False,
                'text' : 'Para criar um login é preciso a parametrização de um senha!'
            }
        paramsNormalize = norm.normalizeParamsInsert(params, self.selectColunas(), self.listOptionsInsertIgnore)
        if not paramsNormalize['response']:
            return {
                'response' : False,
                'text' : paramsNormalize['error']
            }
        sql = f"""
            INSERT INTO {self.table}
                ({paramsNormalize['columns']}, senha)
            VALUES
                ({paramsNormalize['values']}, MD5(%s))"""
        paramsNormalize['params'].append(params['senha'])
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
        paramsNormalize = norm.normalizeParamsUpdate(params, self.selectColunas(), self.listOptionsUpdateIgnore)
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