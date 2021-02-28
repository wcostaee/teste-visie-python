import mysql.connector
import datetime

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
        self.__cursor.execute("SELECT id_pessoa, nome, data_admissao FROM " + self.__table_name)
        return self.__cursor.fetchall()

    def insert(self, data):
        values = (data["nome"], data["rg"], data["cpf"], data["data_nascimento"], data["data_admissao"], data["funcao"])
        query = "INSERT INTO " + self.__table_name \
        + " (nome, rg, cpf, data_nascimento, data_admissao, funcao) " \
        + "VALUES (%s, %s, %s, %s, %s, %s)"
        self.__cursor.execute(query, values)
        self.__db.commit()

    def delete(self, what_id):
        self.__cursor.execute("DELETE FROM " + self.__table_name + " WHERE id_pessoa=" + str(what_id))
        self.__db.commit()

database = Database()
# print(type(database.search_all()[0][1]))
dados = {
    "nome": "Joao",
    "rg": "12345",
    "cpf": "99999999",
    "data_nascimento": '1996-03-10', #AAAA-MM-DD
    "data_admissao": '2021-2-27',
    "funcao": 10
}
# database.insert(dados)
# print(database.search_all())
database.delete(203)