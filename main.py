'''import json
import psycopg2
from flask import Flask, request, make_response


parametros = dict(
    host = 'localhost',
    database = 'Sistema_Medicamentos',
    user = 'postgres',
    password = 'DEUSeuteamo'
)

app = Flask('')
coneccao = psycopg2.connect(**parametros)
cursor = coneccao.cursor()

@app.route('/')
def index():
    return {'nome': request.args.get('name', None),
    'cpf': '123'}

@app.route('/endereco/', methods=['GET'])
def enderecos():
    cursor.execute('select * from endereco;')
    enderecos = cursor.fetchall()
    list_enderecos = []
    for endereco in enderecos:
        list_enderecos.append({
            'rua' : endereco[0],
            'bairro' : endereco[1],
            'numero' : endereco[2],
            'cidade' : endereco[3],
            'cep' : endereco[4]
        })
    return json.dumps(list_enderecos, ensure_ascii=False)

@app.route('/login/', methods=['GET'])
def logins():
    cursor.execute('select * from login;')
    logins = cursor.fetchall()
    list_logins = []
    for login in logins:
        list_logins.append({
            'login' : login[0],
            'senha' : login[1],
        })
    return json.dumps(list_logins, ensure_ascii=False)

@app.route('/lote/', methods=['GET'])
def lotes():
    cursor.execute('select * from Lote;')
    lotes = cursor.fetchall()
    list_lotes = []
    for lote in lotes:
        list_lotes.append({
            'fabricante_id': lote[0],
            'produto_id': lote[1],
            'validade': lote[2],
            'valor': lote[3],
            'codigo_anvisa': lote[4]
        })
    return json.dumps(list_lotes, ensure_ascii=False)


@app.route('/movimentacao/', methods=['GET'])
def movimentacoes():
    cursor.execute('select * from Movimentacao;')
    movimentacoes = cursor.fetchall()
    list_movimentacoes = []
    for movimentacao in movimentacoes:
        list_movimentacoes.append({
            'lote_id': movimentacao[0],
            'tipo': movimentacao[1],
            'data_movimentacao': movimentacao[2],
            'quantidade': movimentacao[3],
            'observacao': movimentacao[4]
        })
    return json.dumps(list_movimentacoes, ensure_ascii=False)


@app.route('/pessoa/', methods=['GET'])
def pessoas():
    cursor.execute('select * from pessoa;')
    pessoas = cursor.fetchall()
    list_pessoas = []
    for pessoa in pessoas:
        list_pessoas.append({
            'tipo': pessoa[0],
            'documento': pessoa[1],
            'nome': pessoa[2],
            'endereco_id': pessoa[3]
        })
    return json.dumps(list_pessoas, ensure_ascii=False)


@app.route('/produto/', methods=['GET'])
def produtos():
    cursor.execute('select * from Produto;')
    produtos = cursor.fetchall()
    list_produtos = []
    for produto in produtos:
        list_produtos.append({
            'nome': produto[0],
            'categoria': produto[1],
        })
    return json.dumps(list_produtos, ensure_ascii=False)


@app.route('/venda/', methods=['GET'])
def vendas():
    cursor.execute('select * from Venda;')
    vendas = cursor.fetchall()
    list_vendas = []
    for venda in vendas:
        list_vendas.append({
            'cliente_id': venda[0],
            'movimentacao_id': venda[1],
            'num_NF': venda[2]
        })
    return json.dumps(list_vendas, ensure_ascii=False)


@app.route('/endereco/add', methods=['POST'])
def new_endereco():
    try:
        rua = request.form.get('rua')
        bairro = request.form.get('bairro')
        numero = request.form.get('numero')
        cidade = request.form.get('cidade')
        cep = request.form.get('cep')
        sql_endereco = ('insert into endereco(rua, bairro, numero, cidade, cep) values (%s, %s, %s, %s, %s)')
        cursor.execute(sql_endereco, (rua, bairro, numero, cidade, cep))
        id = cursor.fetchone()[0]
        cursor.commit()

    except Exception as e:
        print('e', e)
        return make_response('', 388)
    return make_response({'id': id}, 280)


@app.route('/login/add', methods=['POST'])
def new_login():
    try:
        login = request.form.get('login')
        senha = request.form.get('senha')
        sql_login = ('insert into login(login, senha) values (%s, %s)')
        cursor.execute(sql_login, (login, senha))
        id = cursor.fetchone()[0]
        cursor.commit()

    except Exception as e:
        print('e', e)
        return make_response('', 388)
    return make_response({'id': id}, 280)


@app.route('/lote/add', methods=['POST'])
def new_lote():
    try:
        fabricante_id = request.form.get('fabricante_id')
        produto_id = request.form.get('produto_id')
        validade = request.form.get('validade')
        valor = request.form.get('valor')
        codigo_anvisa = request.form.get('codigo_anvisa')
        sql_lote = ('insert into Lote(fabricante_id, produto_id, validade, valor, codigo_anvisa) values (%s, %s, %s, %s, %s)')
        cursor.execute(sql_lote, (fabricante_id, produto_id, validade, valor, codigo_anvisa))
        id = cursor.fetchone()[0]
        cursor.commit()

    except Exception as e:
        print('e', e)
        return make_response('', 388)
    return make_response({'id': id}, 280)


@app.route('/movimentacao/add', methods=['POST'])
def new_movimentacao():
    try:
        lote_id = request.form.get('lote_id')
        tipo = request.form.get('tipo')
        data_movimentacao = request.form.get('data_movimentacao')
        quantidade = request.form.get('quantidade')
        observacao = request.form.get('observacao')
        sql_movimentacao = ('insert into Movimentacao(lote_id, tipo, data_movimentacao, quantidade, observacao) values (%s, %s, %s, %s, %s)')
        cursor.execute(sql_movimentacao, (lote_id, tipo, data_movimentacao, quantidade, observacao))
        id = cursor.fetchone()[0]
        cursor.commit()

    except Exception as e:
        print('e', e)
        return make_response('', 388)
    return make_response({'id': id}, 280)


@app.route("/pessoa/add", methods=['POST'])
def new_pessoa():
    try:
        tipo = request.form.get('tipo')
        documento = request.form.get('documento')
        nome = request.form.get('nome')
        endereco_id = request.form.get('endereco_id')
        sql_pessoa = ("insert into pessoa(tipo, documento, nome, endereco_id) values (%s, %s, %s, %s) RETURNING id")
        cursor.execute(sql_pessoa, (tipo, documento, nome, endereco_id))
        id = cursor.fetchone()[0]
        cursor.commit()

    except Exception as e:
        print('e', e)
        return make_response("", 388)
    return make_response({'id' : id}, 280)


@app.route("/produto/add", methods=['POST'])
def new_produto():
    try:
        nome = request.form.get('nome')
        categoria = request.form.get('categoria')
        sql_produto = ("insert into Produto(nome, categoria) values (%s, %s) RETURNING id")
        cursor.execute(sql_produto, (nome, categoria))
        id = cursor.fetchone()[0]
        cursor.commit()

    except Exception as e:
        print('e', e)
        return make_response("", 388)
    return make_response({'id' : id}, 280)


@app.route("/venda/add", methods=['POST'])
def new_venda():
    try:
        cliente_id = request.form.get('cliente_id')
        movimentacao_id = request.form.get('movimentacao_id')
        num_NF = request.form.get('num_NF')
        sql_venda = ("insert into Venda(cliente_id, movimentacao_id, num_NF) values (%s, %s, %s) RETURNING id")
        cursor.execute(sql_venda, (cliente_id, movimentacao_id, num_NF))
        id = cursor.fetchone()[0]
        cursor.commit()

    except Exception as e:
        print('e', e)
        return make_response("", 388)
    return make_response({'id' : id}, 280)

app.run()'''