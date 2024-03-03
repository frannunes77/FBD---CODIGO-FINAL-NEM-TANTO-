from models.produto.modelo import Produto
from models.produto.sql import SQLProduto
from service.connect import Connect

class DAOProduto(SQLProduto):
    def __init__(self):
        self.connection = Connect().get_instance()


    def create_table(self):
        return self.create_table()

    def salvar(self, produto : Produto):
        if not isinstance(produto, Produto):
            raise Exception("Tipo inválido")

        query = self._INSERT_INTO
        cursor = self.connection.cursor()
        cursor.execute(query, (produto.nome, produto.fabricante_id, produto.lote, produto.validade, produto.valor, produto.condigo_anvisa,))
        self.connection.commit()
        return produto

    def get_all(self):
        query = self._SELECTALL_
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Produto(**i) for i in results]
        return results


    def get_nome_produto(self, nome_produto):
        query = self._SELECT_BY_PRODUTO
        cursor = self.connection.cursor()
        cursor.execute(query, (nome_produto,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Produto(**i) for i in results]
        return results


    def get_fabricante_id_by_produto(self, nome_produto):
        pass

