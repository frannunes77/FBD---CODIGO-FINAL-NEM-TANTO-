from flask import Blueprint, request, jsonify
from models.endereco.dao import DAOEndereco
from models.endereco.modelo import Endereco
from models.endereco.sql import SQLEndereco

endereco_controller = Blueprint('endereco_controller', __name__) #Blueprints: separar as partes (seções) do seu site, como namespaces.
dao_endereco = DAOEndereco()


@endereco_controller.route(f'/todos_enderecos/', methods=['GET'])
def get_Enderecos():
        enderecos = dao_endereco.get_all()
        results = [endereco.__dict__ for endereco in enderecos]
        response = jsonify(results)
        response.status_code = 200
        return response


@endereco_controller.route('/endereco_id/', methods=['GET'])
def getEndereco_byID():
    erros = []

    data = request.json
    meuid = data.get('id')
    endereco_id = dao_endereco.get_endereco_by_id(meuid)

    if not endereco_id:
        erros.append("Não foi encontrado um login com o login fornecido")
        response = jsonify(erros)
        response.status_code = 404
        return response

    results = [endereco.__dict__ for endereco in endereco_id]
    response = jsonify(results)
    response.status_code = 200
    return response


@endereco_controller.route('/criar_enderecos/', methods=['POST'])
def create_login():
    data = request.json
    erros = []

    for campo in SQLEndereco._CAMPOS_OBRIGATORIOS:
        if campo not in data.keys() or not data.get(campo, '').strip():
            erros.append(f"O campo {campo} é obrigatorio")

    if not erros and dao_endereco.endereco_existe(data.get('rua'), data.get('bairro'), data.get('numero'), data.get('cidade'), data.get('cep')):
        erros.append(f"Endereco já existe")


    if erros:
        response = jsonify(erros)
        response.status_code = 401
        return response

    pessoa = Endereco(**data)
    dao_endereco.salvar(pessoa)
    response = jsonify('OK')
    response.status_code = 201
    return response



@endereco_controller.route('/modificar_endereco/', methods=['PUT'])
def update_endereco():
    data = request.json
    erros = []

    if 'rua' not in data and 'bairro' not in data and 'numero' not in data and 'cidade' not in data and 'cep' not in data:
        erros.append('Um dos campos não foi preenchido')

    if erros:
        response = jsonify(erros)
        response.status_code = 401
        return response


    endereco = dao_endereco.endereco_existe(data.get('rua'), data.get('bairro'), data.get('numero'), data.get('cidade'), data.get('cep'))
    if not endereco:
        erros.append("Não foi encontrado um endereco assim")
        response = jsonify(erros)
        response.status_code = 404
        return response

    for endereco_atual in endereco:
        if endereco_atual.rua == data.get('rua') and endereco_atual.bairro == data.get(
                'bairro') and endereco_atual.numero == data.get('numero') and endereco_atual.cidade == data.get(
                'cidade') and endereco_atual.cep == data.get('cep'):
            erros.append("Os novos dados são idênticos aos dados existentes")
            response = jsonify(erros)
            response.status_code = 400
            return response

    endereco_id = dao_endereco.get_id_by_endereco(data.get('rua'), data.get('bairro'), data.get('numero'), data.get('cidade'), data.get('cep'))

    nova_rua = data['nova_rua']
    novo_bairro = data['novo_bairro']
    novo_numero = data['novo_numero']
    nova_cidade = data['nova_cidade']
    novo_cep = data['novo_cep']

    if 'rua' in data and nova_rua!="":
        dao_endereco.atualizar_rua(endereco_id, nova_rua)

    if 'bairro' in data and novo_bairro!="":
        dao_endereco.atualizar_bairro(endereco_id, novo_bairro)

    if 'numero' in data and novo_numero!="":
        dao_endereco.atualizar_bairro(endereco_id, novo_numero)

    if 'cidade' in data and nova_cidade!="":
        dao_endereco.atualizar_bairro(endereco_id, nova_cidade)

    if 'cep' in data and novo_cep!="":
        dao_endereco.atualizar_bairro(endereco_id, novo_cep)

    response = jsonify("Login atualizado com sucesso")
    response.status_code = 200
    return response


@endereco_controller.route('/deletar_endereco/', methods=['DELETE'])
def delete_endereco():
    data = request.json
    endereco_rua = data.get('rua')
    endereco_bairro = data.get('bairro')
    endereco_numero = data.get('numero')
    endereco_cidade = data.get('cidade')
    endereco = dao_endereco.get_id_by_endereco(endereco_rua, endereco_bairro, endereco_numero, endereco_cidade)
    endereco_id = dao_endereco.get_id_by_endereco(endereco)

    if endereco_id is None:
        return jsonify({'error': 'Login não encontrado'}), 404


    dao_endereco.delete_endereco_by_id(endereco_id)
    return jsonify({'message': 'Login excluído com sucesso'}), 200