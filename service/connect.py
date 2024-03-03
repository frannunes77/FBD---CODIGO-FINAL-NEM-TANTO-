import psycopg2

class Connect:

    def __init__(self):
        config = dict(
            dbname="Sistema_Medicamentos",
            user="postgres", password="DEUSeuteamo",
            host="localhost", port="5432"
        )
        self._connection = psycopg2.connect(**config)

    def create_tables(self):
        from models.login.dao import DAOLogin
        from models.endereco.dao import DAOEndereco
        from models.pessoa.dao import DAOPessoa
        from models.produto.dao import DAOProduto
        cursor = self._connection.cursor()
        cursor.execute(DAOLogin().create_table())
        cursor.execute(DAOEndereco().create_table())
        cursor.execute(DAOPessoa().create_table())
        cursor.execute(DAOProduto().create_table())
        self._connection.commit()
        cursor.close()

    def get_instance(self):
        return self._connection

    def init_database(self, version='v1'):
        if version == 'v1':
            self.create_tables()
        if version == 'v2':
            self.update_database()

    def update_database(self):
        pass