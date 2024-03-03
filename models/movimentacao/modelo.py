from models.produto.modelo import Produto


class Movimentacao():
    def __init__(self, produto_id:Produto, tipo, data_movimentacao, quantidade, observacao, id=None):
        self.id = id
        self.produto_id = produto_id
        self.tipo = tipo
        self.data_movimentacao = data_movimentacao
        self.quantidade = quantidade
        self.observacao = observacao
