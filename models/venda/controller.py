from flask import Blueprint, request, jsonify

from models.venda.dao import DAOVenda

venda_controller = Blueprint('venda_controller', __name__)
dao_venda = DAOVenda()


@venda_controller.route(f'/todas_as_vendas/', methods=['GET'])
def get_vendas():
    vendas = dao_venda.get_all()
    results = [venda.__dict__ for venda in vendas]
    response = jsonify(results)
    response.status_code = 200
    return response

