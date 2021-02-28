# Teste prático de Python, HTML e CSS  

## Resumo  
A ideia deste projeto é demonstrar as habilidades necessárias ao cargo de desenvolvedor Full Stack em Python.  
Para cumprir os requisitos do projeto, foram utilizados duas bibliotecas: **Flask** e **mysql-connector-python**. A primeira possui a função de ser um microframework, apenas para lidar com as requisições da interface ao usuário via GET e POST. Já a biblioteca **mysql-connector-python** é responsável por ser um driver de acesso ao banco de dados MySQL hospedado no website [db4free](https://db4free.net/).  

## Como testar  
Este projeto foi criado no **Ubuntu 20.04** e **Python 3.8.5**. Para testar, é recomendado utilizar um ambiente virtual Python. Considerando que o seu diretório atual é **/teste-visie-python**, execute:  
```
cd ..
python3 -m venv env
```
Isso criará uma pasta chamada **env** no diretório atual (acima de **teste-visie-python**). Para ativar este ambiente, execute:  
```
source ./env/bin/activate
```
Instale as dependências deste projeto (precisa de Internet). Para isso, execute:
```
cd teste-visie-python
pip install -r requirements.txt
```
O framework Flask precisa saber onde está o script principal. Para isso, execute:  
```
export FLASK_APP=main.py
```
Para iniciar o servidor, execute:  
```
flask run
```
Acesse, no seu navegador, **localhost:5000** e você verá a interface da aplicação.
