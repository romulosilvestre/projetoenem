#vou importar a classe Flask do pacote flask
#o make_response geralmente gera em JSON
from flask import Flask,make_response,jsonify,request
from dados import Materias

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
    #response
    return make_response(
        jsonify(Materias)
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
