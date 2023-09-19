from mysql.connector import Error
import mysql.connector
import sys

def connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='Gustakx36.mysql.pythonanywhere-services.com',
            user='Gustakx36', #'root'
            passwd='Gg1234klkl', #''
            database='Gustakx36$hamburgueria',
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
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Error as err:
        print( "Error: " + str(err))
        return False

def read_query_bind(query, bind, onlyOne):
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, bind)
        if onlyOne:
            return cursor.fetchone()
        return cursor.fetchall()
    except Error as err:
        print( "Error: " + str(err))
        return False