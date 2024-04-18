#vou importar a classe Flask do pacote flask
#o make_response geralmente gera em JSON
from flask import Flask,make_response,jsonify,request
from dados import Materias
import mysql.connector #importando o conector

#variável para conexão
#host - é o servidor
#user - usuário
#senha - root
#database - enem
mydb = mysql.connector.connect(
   host = 'localhost',
   user = 'root',
   password= 'root',
   database = 'enemteste',
)
#SQL no Python
#SELECT * FROM materias
#FIXME:INSERT INTO ... (parei aqui! 17/04)

#FIXME: Flask é um classe
#instâciando o objeto app
#Assume o nome da aplicação como nome padrão
app = Flask("__name__")
#NOTE: vamos decorar
#exemplo sem decorar
#será que o flask consegue entender essa função solta ai?
#POST(inserir),PUT(atualizar),GET,DELETE
@app.route('/materias',methods=['GET'])
def get_materias():
    #NOTE: crie o cursor para executar SQL
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM materias")
    #retornar a lista de todas as materiais
    minhas_materiais=my_cursor.fetchall()
    #response
    return make_response(
        jsonify(
            mensagem = "lista de matérias cadastradas",
            dados = minhas_materiais
        )
    ) 

@app.route("/")
def index():
    return "Projeto Integrador Base (Enem)"


#request
#POST
@app.route('/materias',methods=['POST'])
def create_materia():
    materia = request.json
    return materia


#executar a API
app.run()
