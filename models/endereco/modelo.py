class Endereco():
    def __init__(self, rua, bairro, numero, cidade, cep, id=None):
        self.id = id
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.cidade = cidade
        self.cep = cep

    def __str__(self):
        return ('Rua: {}, {}, nº {} - {} - CEP: {}'.format(self.rua, self.bairro, self.numero, self.cidade, self.cep))
