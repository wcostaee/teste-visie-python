from flask import Flask, url_for, render_template, redirect, request
from database import Database

app = Flask(__name__)

@app.route("/")
def main():
    '''Caminho principal: mostra a pagina inicial da aplicacao'''
    db = Database() #Cria um objeto do banco de dados
    data = db.search_all() #Busca todos os registros do banco de dados
    data_formatted = [] #Armazena os dados formatados
    for each in data:
        data_formatted.append(format_data(each))
    #Retorna os dados formatados para serem renderizados
    return render_template("home.html", data_formatted=data_formatted) 

@app.route("/delete/<id_person>", methods=["POST"])
def delete(id_person):
    '''Caminho para deletar um registro do banco de dados'''
    db = Database() #Cria um objeto do banco de dados
    db.delete(int(id_person))
    return redirect(url_for("main")) #Redireciona a pagina inicial com os registros ja atualizados

@app.route("/add_person", methods=["POST"])
def add():
    '''Caminho para adicionar um registro'''
    try: #Caso haja problema na conversao dos dados, uma excecao do tipo ValueError sera levantada
        info = {
            "nome": str(request.form.get("name")),
            "rg": str(request.form.get("rg")),
            "cpf": str(request.form.get("cpf")),
            "data_admissao": str(request.form.get("first_day_work")),
            "data_nascimento": str(request.form.get("birthday")),
            "funcao": int(request.form.get("role"))
        }
        db = Database() #Cria um objeto do banco de dados
        db.insert(info) #A conversao deu certo. Adicione no banco de dados
    except ValueError as err: #Houve um erro durante a conversao. Exibe o tipo de erro
        print("Dados invalidos: ", err)
    return redirect(url_for("main")) #Redireciona a pagina inicial (tendo dado certo ou errado)

def format_data(data):
    '''Formata os dados que vieram do banco de dados. Espera-se um tuple como "data" e com 3 posicoes.'''
    if len(data) == 3: #O registro esta certo? (id, nome, data de admissao)
        if data[1] is None: #O nome é NULL no banco de dados
            name = "-" #Apenas mostre '-'
        else:
            name = (str(data[1])).split()[0] #O nome sera quebrado por espaco e pegue apenas o primeiro nome
                                            #Exemplo: nome="Joao da Silva" => ["Joao", "da", "Silva"]
        if data[2] is None: #Nao tem data de admissao
            date = "Indefinido" #Exibe 'Indefinido'
        else:
            temp = (str(data[2])).split("-") #Quebra a data por hifen (resultado: ["AAAA", "MM", "DD"])
            if len(temp) == 3: #A data tem tres termos?
                date = temp[2] + "/" + temp[1] + "/" + temp[0] #Reordene para o padrao brasileiro
            else:
                date = "Indefinido" #Havia um erro no registro. Apenas mostre 'Indefinido'
        return (data[0], name, date) #Retorna um tuple