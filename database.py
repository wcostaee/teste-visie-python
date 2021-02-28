import mysql.connector

class Database:
    def __init__(self):
        host = "db4free.net" #Define onde está o banco de dados
        user = "visie_user" #Nome de usuario
        password = "visie_pass" #Senha
        self.__db = mysql.connector.connect(host=host, user=user, password=password)
        self.__cursor = self.__db.cursor()

database = Database()