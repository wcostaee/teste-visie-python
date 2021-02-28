import mysql.connector #Conector responsável por acessar o banco de dados online

class Database:
    '''Criação do objeto Database, responsável por todas as manipulações necessárias ao banco de dados'''
    def __init__(self):
        host = "db4free.net" #Define onde está o banco de dados
        user = "visie_user" #Nome de usuario
        password = "visie_pass" #Senha
        db_name = "visie_db" #Nome do banco de dados
        self.__table_name = "pessoas" #Em qual tabela a busca será feita
        self.__db = mysql.connector.connect(host=host, user=user, password=password, database=db_name)
        self.__cursor = self.__db.cursor()

    def search_all(self):
        '''Busca todos os registros no banco de dados. Retorna um vetor de tuple (id_pessoa, nome, data_admissao)'''
        self.__cursor.execute("SELECT id_pessoa, nome, data_admissao FROM " + self.__table_name)
        return self.__cursor.fetchall()

    def insert(self, data):
        '''Insere um novo registro no banco de dados. Recebe um dicionário com as seguintes chaves:
        nome, rg, cpf, data_nascimento, data_admissao e funcao'''
        values = (data["nome"], data["rg"], data["cpf"], data["data_nascimento"], data["data_admissao"], data["funcao"])
        query = "INSERT INTO " + self.__table_name \
                + " (nome, rg, cpf, data_nascimento, data_admissao, funcao) " \
                + "VALUES (%s, %s, %s, %s, %s, %s)"
        self.__cursor.execute(query, values)
        self.__db.commit()

    def delete(self, what_id):
        '''Apaga um registro do banco de dados através da id_pessoa'''
        self.__cursor.execute("DELETE FROM " + self.__table_name + " WHERE id_pessoa=" + str(what_id))
        self.__db.commit()

## Descomente alguma parte do código abaixo para testar alguma funcionalidade desta classe
# database = Database()
# print(type(database.search_all())
# dados = {
#     "nome": "Joao",
#     "rg": "12345",
#     "cpf": "99999999",
#     "data_nascimento": '1996-03-10', #AAAA-MM-DD
#     "data_admissao": '2021-2-27',
#     "funcao": 10
# }
# database.insert(dados)
# database.delete(203)