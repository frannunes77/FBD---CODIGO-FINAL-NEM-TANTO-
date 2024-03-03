from models.venda.modelo import Venda
from models.venda.sql import SQLVenda
from service.connect import Connect


class DAOVenda(SQLVenda):
    def __init__(self):
        self.connection = Connect().get_instance()


    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, venda:Venda):
        if not isinstance(venda, Venda):
            raise Exception("Tipo inválido")

        query = self._INSERT_INTO
        cursor = self.connection.cursor()
        cursor.execute(query, (venda.cliente_id, venda.movimentacao_id, venda.num_NF,))
        self.connection.commit()
        return venda

    def get_all(self):
        query = self._SELECET_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Venda(**i) for i in results]
        return results




