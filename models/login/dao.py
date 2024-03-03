from models.login.modelo import Login
from models.login.sql import SQLLogin
from service.connect import Connect


class DAOLogin(SQLLogin):
    def __init__(self, ):
        self.connection = Connect().get_instance()  # É feito a conexao

    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, login: Login):
        if not isinstance(login, Login):  # retorna se o objeto é do tipo
            raise Exception("Tipo inválido")  # Para lançar uma exceção de dentro de uma função ou método

        query = self._INSERT_INTO  # query --> solicitação de informações a um banco de dados
        cursor = self.connection.cursor()
        cursor.execute(query, (login.login, login.senha))
        self.connection.commit()  # .commit() : usado para fazer as transações/mudanças no DB
        return login


    def get_all_antigo(self):
        query = self._SELECT_BY_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Login(**i) for i in results]
        return results

    def get_by_meulogin_antigo(self, login):  # ver quais serão as informações
        query = self._SELECT_BY_LOGIN  # VER ISSO AQUI POIS VER O QUE VAI PEGAR MESMO
        cursor = self.connection.cursor()
        cursor.execute(query, (login,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        results = [Login(**i) for i in results]
        return results

    def get_id_by_login(self, login):
        query = self._SELECT_BY_LOGIN
        cursor = self.connection.cursor()
        cursor.execute(query, (f"%{login}%",))
        result = cursor.fetchone()
        if result:
            return result[0]  # O ID é o primeiro valor retornado
        else:
            return None


    def atualizar_login(self, login_id, novo_login):
        query = self._UPDATE_BY_LOGIN
        cursor = self.connection.cursor()
        cursor.execute(query, (novo_login, login_id))
        self.connection.commit()


    def atualizar_senha(self, login_id, nova_senha):
        query = self._UPDATE_BY_SENHA
        cursor = self.connection.cursor()
        cursor.execute(query, (nova_senha, login_id))
        self.connection.commit()


    def delete_login_by_id(self, login_id):
        query = self._DELETE_BY_LOGIN
        cursor = self.connection.cursor()
        cursor.execute(query, (login_id,))
        self.connection.commit()

