from flask import Blueprint, request, jsonify
from models.movimentacao.dao import DAOMovimentacao


movimentacao_controller = Blueprint('movimentacao_controller', __name__)
dao_movimentacao = DAOMovimentacao()


@movimentacao_controller.route(f'/todos_os_movimentos/', methods=['GET'])
def get_movimentos():
    movimentos = dao_movimentacao.get_all()
    results = [movimentacao.__dict__ for movimentacao in movimentos]
    response = jsonify(results)
    response.status_code = 200
    return response


