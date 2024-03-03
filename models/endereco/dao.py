from models.endereco.modelo import Endereco
from models.endereco.sql import SQLEndereco
from service.connect import Connect

class DAOEndereco(SQLEndereco):
        def __init__(self, ):
                self.connection = Connect().get_instance()


        def create_table(self):
                return self._CREATE_TABLE


        def salvar(self, endereco : Endereco):
                if not isinstance(endereco, Endereco): # retorna se o objeto é do tipo
                        raise Exception("Tipo inválido")   # Para lançar uma exceção de dentro de uma função ou método

                query = self._INSERT_INTO  # query --> solicitação de informações a um banco de dados
                cursor = self.connection.cursor()
                cursor.execute(query, (endereco.rua, endereco.bairro, endereco.numero, endereco.cidade, endereco.cep,))
                self.connection.commit() # .commit() : usado para fazer as transações/mudanças no DB
                return endereco


        def get_all(self):
                query = self._SELECT_ALL
                cursor = self.connection.cursor()
                cursor.execute(query)
                results = cursor.fetchall()
                cols = [desc[0] for desc in cursor.description]
                results = [dict(zip(cols, i)) for i in results]
                results = [Endereco(**i) for i in results]
                return results


        def get_endereco_by_id(self, endereco_id):
                query = self._SELECT_ID
                cursor = self.connection.cursor()
                cursor.execute(query, (endereco_id,))
                results = cursor.fetchall()
                cols = [desc[0] for desc in cursor.description]
                results = [dict(zip(cols, i)) for i in results]
                results = [Endereco(**i) for i in results]
                return results


        def endereco_existe(self, rua, bairro, numero, cidade, cep):
                query = self._SELECT_BY_DADOS
                cursor = self.connection.cursor()
                cursor.execute(query, (rua, bairro, numero, cidade, cep))
                resultado = cursor.fetchone()
                return resultado[0] > 0


        def get_id_by_endereco(self, rua, bairro, numero, cidade, cep):
                query = self._SELECT_ID_BY_ENDERECO
                cursor = self.connection.cursor()
                cursor.execute(query, (rua, bairro, numero, cidade, cep))
                results = cursor.fetchone()
                endereco_id = results[0]
                self.connection.commit()
                return endereco_id


        def atualizar_rua(self, endereco_id, nova_rua):
                query = self._UPDATE_BY_RUA
                cursor = self.connection.cursor()
                cursor.execute(query, (endereco_id, nova_rua))
                self.connection.commit()


        def atualizar_bairro(self, endereco_id, novo_bairro):
                query = self._UPDATE_BY_BAIRRO
                cursor = self.connection.cursor()
                cursor.execute(query, (endereco_id, novo_bairro))
                self.connection.commit()


        def atualizar_numero(self, endereco_id, novo_numero):
                query = self._UPDATE_BY_NUMERO
                cursor = self.connection.cursor()
                cursor.execute(query, (endereco_id, novo_numero))
                self.connection.commit()


        def atualizar_cidade(self, endereco_id, nova_cidade):
                query = self._UPDATE_BY_CIDADE
                cursor = self.connection.cursor()
                cursor.execute(query, (endereco_id, nova_cidade))
                self.connection.commit()


        def atualizar_cep(self, endereco_id, novo_cep):
                query = self._UPDATE_BY_CEP
                cursor = self.connection.cursor()
                cursor.execute(query, (endereco_id, novo_cep))
                self.connection.commit()


        def delete_endereco_by_id(self, endereco_id):
                query = self._DELETE_BY_ENDERECO
                cursor = self.connection.cursor()
                cursor.execute(query, (endereco_id,))
                self.connection.commit()
