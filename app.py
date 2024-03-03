from flask import Flask
from models.login.controller import login_controller
from models.endereco.controller import endereco_controller
from models.movimentacao.controller import movimentacao_controller
from models.pessoa.controller import pessoa_controller
from models.produto.controller import produto_controller
from models.venda.controller import venda_controller
from service.connect import Connect

app = Flask(__name__)
app.register_blueprint(login_controller)
app.register_blueprint(endereco_controller)
app.register_blueprint(pessoa_controller)
app.register_blueprint(produto_controller)
app.register_blueprint(movimentacao_controller)
app.register_blueprint(venda_controller)
Connect().init_database('v2')
app.run(debug=True)