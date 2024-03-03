from flask import Blueprint, request, jsonify
from models.pessoa.dao import DAOPessoa
from models.pessoa.modelo import Pessoa
from models.pessoa.sql import SQLPessoa

pessoa_controller = Blueprint('pessoa_controller', __name__)
dao_pessoa = DAOPessoa()


@pessoa_controller.route(f'/todas_as_pessoas/', methods=['GET'])
def get_pessoas():
    pessoas = dao_pessoa.get_all()
    results = [pessoa.__dict__ for pessoa in pessoas]
    response = jsonify(results)
    response.status_code = 200
    return response

@pessoa_controller.route('/endereco_by_pessoa/', methods=['GET'])
def get_endereco_by_pessoa():
    erros = []

    data = request.json
    nome_pessoa = data.get('nome')
    enderecos = dao_pessoa.get_endereco_by_NomePessoa(nome_pessoa)

    if not enderecos:
        erros.append("Não foi encontrado um login com o login fornecido")
        response = jsonify(erros)
        response.status_code = 404
        return response

    results = [endereco.__dict__ for endereco in enderecos]
    response = jsonify(results)
    response.status_code = 200
    return response


@pessoa_controller.route('/criar_pessoa/', methods=['POST'])
def create_pessoa():
    data = request.json
    erros = []

    if not erros and dao_pessoa.get_id_by_nome(data.get('tipo'), data.get('documento'), data.get('nome')):
        erros.append(f"Já existe! Por favor, verifica a nova pessoa a ser criada")

    if dao_pessoa.get_endereco_by_NomePessoa(data.get('nome')):
        erros.append(f"Esse endereço já esta inserido, por favor, verifica se o mesmo está correto.")

    if erros:
        response = jsonify(erros)
        response.status_code = 401
        return response

    pessoa = Pessoa(**data)
    dao_pessoa.salvar(pessoa)
    response = jsonify('OK')
    response.status_code = 201
    return response