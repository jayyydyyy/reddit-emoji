import mysql.connector

class MySQL_Repo:
    def __init__(self) -> None:
        config = {
            'user' : 'root',
            'password': 'root',
            'host' : 'mysql',
            'port' : '3306',
            'host' : 'localhost',
            'port' : '32000',
            'database':'reddit'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        return list(self.cursor)
    
    def initialize(self):
        init_sql = ''
        with open('./data/init.sql') as f:
            init_sql = f.read()
        self.execute(init_sql)