from models.endereco.modelo import Endereco
from models.pessoa.modelo import Pessoa
from models.pessoa.sql import SQLPessoa
from service.connect import Connect


class DAOPessoa(SQLPessoa):
    def __init__(self):
        self.connection = Connect().get_instance()


    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, pessoa : Pessoa):
        if not isinstance(pessoa, Pessoa):
            raise Exception("Tipo inválido")

        query = self._INSERT_INTO
        cursor = self.connection.cursor()
        cursor.execute(query, (pessoa.tipo, pessoa.documento, pessoa.nome, pessoa.endereco_id))
        self.connection.commit()
        return pessoa

    def get_all(self):
        query = self._SELECET_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Pessoa(**i) for i in results]
        return results


    def get_endereco_by_NomePessoa(self, nome_pessoa):
        query = self._SELECT_ENDERECO_BY_NOME
        cursor = self.connection.cursor()
        cursor.execute(query, (nome_pessoa,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Endereco(**i) for i in results]
        return results

    def get_id_by_nome(self, tipo_pessoa, documento_pessoa, nome_pessoa):
        query = self._SELECT_ID_BY_NOME_TIPO
        cursor = self.connection.cursor()
        cursor.execute(query, (tipo_pessoa, documento_pessoa, nome_pessoa,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Endereco(**i) for i in results]
        return results


