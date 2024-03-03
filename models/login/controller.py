from flask import Blueprint, request, jsonify
from models.login.dao import DAOLogin
from models.login.modelo import Login
from models.login.sql import SQLLogin

login_controller = Blueprint('login_controller', __name__) #Blueprints: separar as partes (seções) do seu site, como namespaces.
dao_login = DAOLogin()


@login_controller.route('/todos_logins/', methods=['GET'])
def get_logins():
    data = request.json
    print(data)
    logins = dao_login.get_all_antigo()
    results = [login.__dict__ for login in logins]
    response = jsonify(results)
    response.status_code = 200
    return response


@login_controller.route('/criar_login/', methods=['POST'])
def create_login():
    data = request.json
    erros = []
    for campo in SQLLogin._CAMPOS_OBRIGATORIOS:
        if campo not in data.keys() or not data.get(campo, '').strip():
            erros.append(f"O campo {campo} é obrigatorio")

    if not erros and dao_login.get_by_meulogin_antigo(data.get('login')):
        erros.append(f"Já existe um login com essa descrição")
    if erros:
        response = jsonify(erros)
        response.status_code = 401
        return response

    login = Login(**data)
    dao_login.salvar(login)
    response = jsonify('OK')
    response.status_code = 201
    return response


@login_controller.route('/atualizar_login/', methods=['PUT'])
def update_login():
    data = request.json
    erros = []

    if 'login' not in data and 'senha' not in data:
        erros.append("Pelo menos um dos campos 'login' ou 'senha' deve ser fornecido para atualização")


    if erros:
        response = jsonify(erros)
        response.status_code = 401
        return response


    login = data.get('login')
    login_id = dao_login.get_id_by_login(login)
    if not login_id:
        erros.append("Não foi encontrado um login com o login fornecido")
        response = jsonify(erros)
        response.status_code = 404
        return response

    novo_login = data['novo_login']
    nova_senha = data['nova_senha']
    print(novo_login)
    print(nova_senha)


    if 'login' in data and novo_login!="":
        dao_login.atualizar_login(login_id, novo_login)

    if 'login' in data and 'senha' in data and nova_senha!="":
        dao_login.atualizar_senha(login_id, nova_senha)

    response = jsonify("Login atualizado com sucesso")
    response.status_code = 200
    return response


@login_controller.route('/delete_login/', methods=['DELETE'])
def delete_login():
    data = request.json
    login = data.get('login')
    login_id = dao_login.get_id_by_login(login)
    if login_id is None:
        return jsonify({'error': 'Login não encontrado'}), 404

    # Caso contrário, exclua o login do banco de dados usando o ID obtido
    # Retorne uma mensagem indicando que o login foi excluído com sucesso
    dao_login.delete_login_by_id(login_id)
    return jsonify({'message': 'Login excluído com sucesso'}), 200


