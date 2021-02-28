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

## Detalhes de implementação  
Durante o desenvolvimento desta aplicação, tomou-se o cuidado para torná-la o mais simples possível e suficiente para atender aos requisitos de projeto. Dessa forma, não se teve preocupação com detalhes que seriam importantes em uma aplicação real.  
O microframework **Flask** utiliza um sistema de *template* através da biblioteca **Jinja2** (instalada como dependência do **Flask**). Este sistema permite a manipulação de objetos diretamente no arquivo HTML. Dessa forma, ao renderizar a página principal, passa-se um objeto com os registros das pessoas e, dentro do arquivo HTML, existe um *loop* **for** para exibir os dados dos registros. Exemplo:
```
{% for dado in dados %}
<p>{{dado[0]}}</p>
{% endfor %}
```
No exemplo acima, considere que *dados* é um vetor e cada membro dele é um tuple. Ao navegar em cada item de *dados*, é possível acessar a posição *0* do tuple e exibir esta informação diretamente no arquivo HTML.  
Outro ponto importante é o botão "Excluir". A partir da renderização, ele consegue saber qual a *id* da pessoa a qual ele se refere. Dessa forma, se uma determinada linha representa uma pessoa com *id* igual a 1, o botão fará um *submit* no endereço ```/delete/1```, deletando o registro 1.  

## Resultado  
Caso você queira ver a aplicação em funcionamento, acesse [este link](https://youtu.be/1ghWKsBgXAk) para uma demonstração.
