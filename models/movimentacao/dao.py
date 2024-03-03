from models.movimentacao.modelo import Movimentacao
from models.movimentacao.sql import SQLMovimentacao
from service.connect import Connect

class DAOMovimentacao(SQLMovimentacao):
    def __init__(self):
        self.connection = Connect().get_instance()


    def create_table(self):
        return self.create_table()

    def salvar(self, movimentacao : Movimentacao):
        if not isinstance(movimentacao, Movimentacao):
            raise Exception("Tipo inválido")

        query = self._INSERT_INTO
        cursor = self.connection.cursor()
        cursor.execute(query, (movimentacao.produto_id, movimentacao.tipo, movimentacao.data_movimentacao, movimentacao.quantidade, movimentacao.observacao,))
        self.connection.commit()
        return movimentacao

    def get_all(self):
        query = self._SELECTALL_
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Movimentacao(**i) for i in results]
        return results


    def get_endereco_by_NomePessoa(self, nome_pessoa):
        pass