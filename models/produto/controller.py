from flask import Blueprint, request, jsonify
from models.produto.dao import DAOProduto
from models.produto.sql import SQLProduto

produto_controller = Blueprint('produto_controller', __name__)
dao_produtos = DAOProduto()


@produto_controller.route(f'/todos_os_produtos/', methods=['GET'])
def get_produtos():
    produtos = dao_produtos.get_all()
    results = [produto.__dict__ for produto in produtos]
    response = jsonify(results)
    response.status_code = 200
    return response


'''@produto_controller.route('/produto_criar/', methods=['POST'])
def create_produto():
    data = request.json
    erros = []
    for campo in SQLProduto._CAMPOS_OBRIGATORIOS:
        if campo not in data.keys() or not data.get(campo, '').strip():
            erros.append(f"O campo {campo} é obrigatorio")

    if not erros and dao_produtos.get_nome_produto(data.get('nome')) and :
        erros.append(f"Já existe um prdouto e fabricante com essas descrições")

    if erros:
        response = jsonify(erros)
        response.status_code = 401
        return response

    login = Login(**data)
    dao_login.salvar(login)
    response = jsonify('OK')
    response.status_code = 201
    return response'''

