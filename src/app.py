from flask import Flask
from decouple import config
from modelo.Pacientes import ModeloPaciente
from config import config

app = Flask(__name__)

# RUTA PARA PETICION GET

@app.route("/")
def hello_world():
    return  " hola mundo "

#mostrar todos los pacientes
@app.route("/pacientes", methods=['GET'])
def listar_pacientes():
    resul=ModeloPaciente.listar_Paciente()
    return resul

#buscar solo un paciente
@app.route("/pacientes/:<codigo>", methods=['GET'])
def lista_paciente(codigo):
    resul=ModeloPaciente.lista_Paciente(codigo)
    return resul

#registrar paciente
@app.route("/pacientes",methods=['POST'])
def guardar_paciente():
    resul=ModeloPaciente.registrar_paciente()
    return resul


#actualizar paciente
@app.route("/pacientes/:<codigo>",methods=['PUT'])
def actualizxar_paciente(codigo):
    resul=ModeloPaciente.actualizar_paciente(codigo)
    return resul


#eliminar paciente
@app.route("/pacientes/:<codigo>",methods=['DELETE'])
def elimineycion_paciente(codigo):
    resul=ModeloPaciente.eliminar_paciente(codigo)
    return resul

def pag_noencontrada(error):
    return "<h1>Página no Encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pag_noencontrada)
    app.run(host='0.0.0.0')