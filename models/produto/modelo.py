from models.pessoa.modelo import Pessoa

class Produto():
    def __init__(self, nome, fabricante_id : Pessoa, lote, validade, valor, codigo_anvisa, id=None):
        self.id = id
        self.nome = nome
        self.fabricante_id = fabricante_id
        self.lote = lote
        self.validade = validade
        self.valor = valor
        self.codigo_anvisa = codigo_anvisa
