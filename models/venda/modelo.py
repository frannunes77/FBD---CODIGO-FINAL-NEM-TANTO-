from models.movimentacao.modelo import Movimentacao
from models.pessoa.modelo import Pessoa


class Venda():
    def __init__(self, cliente_id : Pessoa, movimentacao_id : Movimentacao, num_nf, id=None):
        self.id = id
        self.cliente_id = cliente_id
        self.movimentacao_id = movimentacao_id
        self.num_nf = num_nf
