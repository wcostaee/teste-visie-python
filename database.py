import mysql.connector

class Database:
    def __init__(self):
        host = "db4free.net" #Define onde está o banco de dados
        user = "visie_user" #Nome de usuario
        password = "visie_pass" #Senha
        db_name = "visie_db" #Nome do banco de dados
        self.__table_name = "pessoas" #Em qual tabela a busca será feita
        self.__db = mysql.connector.connect(host=host, user=user, password=password, database=db_name)
        self.__cursor = self.__db.cursor()

    def search_all(self):
        self.__cursor.execute("SELECT nome, data_admissao FROM " + self.__table_name)
        return self.__cursor.fetchall()

database = Database()
print(database.search_all())