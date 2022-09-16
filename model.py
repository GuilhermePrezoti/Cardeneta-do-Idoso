import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()
        self.db_connection = self.db_connection.conectar
        self.con = self.db_connection.cursor()