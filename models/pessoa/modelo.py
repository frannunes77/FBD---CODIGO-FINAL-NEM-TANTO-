from models.endereco.modelo import Endereco

class Pessoa():
    def __init__(self, tipo, documento, nome, endereco_id : Endereco, id=None):
        self.id = id
        self.tipo = tipo
        self.documento = documento
        self.nome = nome
        self.endereco_id = endereco_id