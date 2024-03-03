class Login():
    def __init__(self, login, senha, id=None):
        self.id = id
        self.login = login
        self.senha = senha

    def __str__(self):
        return ('login : {} \nSenha : {}'.format(self.login, self.senha))


