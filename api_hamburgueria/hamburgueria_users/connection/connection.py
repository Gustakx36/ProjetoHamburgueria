import mysql.connector
from mysql.connector import Error
import sys

def connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root', #'root'
            passwd='', #''
            database='hamburgueria',
            port='3306'
        )
        return connection
    except Error:
        sys.exit()

def execute_query(query, bind):
    conn = connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, bind)
        conn.commit()
        return True
    except Error as err:
        print( "Error: " + str(err))
        return False

def read_query(query):
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Error as err:
        print("Error: " + str(err))
        return "Error: " + str(err)

def read_query_bind(query, bind):
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query, bind)
        return cursor.fetchone()
        return result
    except Error as err:
        print("Error: " + str(err))
        return "Error: " + str(err)

def iniciarTable():
    sqlTable1 = """
        CREATE TABLE IF NOT EXISTS core_cliente
            (
                id INT NULL AUTO_INCREMENT ,
                nome VARCHAR(255) NOT NULL ,
                idade TINYINT NOT NULL ,
                id_login INT NOT NULL ,
                PRIMARY KEY (id)
            )
        ENGINE = InnoDB;
    """
    sqlTable2 = """
        CREATE TABLE IF NOT EXISTS core_api_key
            (
                id INT NULL AUTO_INCREMENT ,
                api_key VARCHAR(40) NULL ,
                id_login INT NOT NULL ,
                PRIMARY KEY (id), UNIQUE (api_key)
            )
        ENGINE = InnoDB;
    """
    sqlTable3 = """
        CREATE TABLE IF NOT EXISTS core_logins
            (
                id INT NOT NULL AUTO_INCREMENT ,
                login VARCHAR(255) NOT NULL ,
                senha VARCHAR(255) NOT NULL ,
                PRIMARY KEY (id)
            )
        ENGINE = InnoDB;
    """
    sqlTable4 = """
        CREATE TABLE IF NOT EXISTS core_endereco
            (
                id INT NOT NULL AUTO_INCREMENT ,
                cep VARCHAR(8) NOT NULL ,
                rua VARCHAR(255) NOT NULL ,
                numero VARCHAR(255) NOT NULL ,
                id_cliente INT NOT NULL ,
                PRIMARY KEY (id)
            ) 
        ENGINE = InnoDB;
    """
    sqlAlter1 = """
        ALTER TABLE core_cliente ADD CONSTRAINT ClienteDeLogin
            FOREIGN KEY (id_login) REFERENCES core_logins(id)
        ON DELETE CASCADE ON UPDATE CASCADE;
    """
    sqlAlter2 = """
        ALTER TABLE core_endereco ADD CONSTRAINT EnderecoDeCliente 
            FOREIGN KEY (id_cliente) REFERENCES core_cliente(id) 
        ON DELETE CASCADE ON UPDATE CASCADE;
    """
    sqlAlter3 = """
        ALTER TABLE core_api_key ADD CONSTRAINT KeyDeLogin 
            FOREIGN KEY (id_login) REFERENCES core_logins(id) 
        ON DELETE CASCADE ON UPDATE CASCADE;
    """
    execute_query(sqlTable1, [])
    execute_query(sqlTable2, [])
    execute_query(sqlTable3, [])
    execute_query(sqlTable4, [])
    execute_query(sqlAlter1, [])
    execute_query(sqlAlter2, [])
    execute_query(sqlAlter3, [])
