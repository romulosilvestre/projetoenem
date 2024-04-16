#vou importar a classe Flask do pacote flask
from flask import Flask
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
    return Materias

#executar a API
app.run()
