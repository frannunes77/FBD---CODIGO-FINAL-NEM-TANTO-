from models.pessoa.sql import SQLPessoa

class SQLProduto:
    _TABELA_ = 'Produto'
    _COLUNA_ID = 'id'
    _COLUNA_NOME = 'nome'
    _COLUNA_FABRICANTE_ID = 'fabricante_id'
    _COLUNA_LOTE = 'lote'
    _COLUNA_VAlIDADE = 'validade'
    _COLUNA_VALOR = 'valor'
    _COLUNA_NUMERO_ANVISA = 'codigo_anvisa'

    _CAMPOS_OBRIGATORIOS = [_COLUNA_NOME, _COLUNA_FABRICANTE_ID, _COLUNA_LOTE, _COLUNA_VAlIDADE, _COLUNA_VALOR, _COLUNA_NUMERO_ANVISA]

    _REFERENCES_ENDERECO = f'{SQLPessoa._TABLE_NAME}({SQLPessoa._COL_ID})'

    _CREATE_TABLE = f'create table if not exists {_TABELA_}' \
                    f'({_COLUNA_ID} serial primary key, ' \
                    f'{_COLUNA_NOME} varchar(50), ' \
                    f'{_COLUNA_FABRICANTE_ID} integer references {_REFERENCES_ENDERECO},' \
                    f'{_COLUNA_LOTE} varchar(50),' \
                    f'{_COLUNA_VAlIDADE} date, ' \
                    f'{_COLUNA_VALOR} decimal, ' \
                    f'{_COLUNA_NUMERO_ANVISA} varchar(13));'

    _INSERT_INTO = f'insert into {_TABELA_}({_COLUNA_NOME}, {_COLUNA_FABRICANTE_ID}, {_COLUNA_LOTE}, ' \
                    f'{_COLUNA_VAlIDADE}, {_COLUNA_VALOR}, {_COLUNA_NUMERO_ANVISA} values (%s, %s, %s, %s, %s, %s)'

    _SELECTALL_ = f'select * from {_TABELA_};'
    _SELECT_BY_PRODUTO = f'select {_COLUNA_NOME} from {_TABELA_} where {_COLUNA_FABRICANTE_ID}=%s;'