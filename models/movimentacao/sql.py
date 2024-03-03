from models.produto.sql import SQLProduto


class SQLMovimentacao:
    _TABELA_ = 'Movimentacao'
    _COLUNA_ID = 'id'
    _COLUNA_PRODUTO_ID = 'produto_id'
    _COLUNA_TIPO = 'tipo'
    _COLUNA_DATA_MOVIMENTACAO = 'data_movimentacao'
    _COLUNA_QUANTIDADE = 'quantidade'
    _COLUNA_OBSERVACAO = 'observacao'

    _REFERENCES_PRODUTO = f'{SQLProduto._TABELA_}({SQLProduto._COLUNA_ID})'

    _CREATE_TABLE = f'create table if not exists {_TABELA_}' \
                    f'({_COLUNA_ID} serial primary key, ' \
                    f'{_COLUNA_PRODUTO_ID} integer references {_REFERENCES_PRODUTO}, ' \
                    f'{_COLUNA_TIPO} varchar(50), ' \
                    f'{_COLUNA_DATA_MOVIMENTACAO} date, ' \
                    f'{_COLUNA_QUANTIDADE} integer, ' \
                    f'{_COLUNA_OBSERVACAO} varchar(20);'

    _INSERT_INTO = f'insert into {_TABELA_}({_COLUNA_PRODUTO_ID}, {_COLUNA_TIPO}, {_COLUNA_DATA_MOVIMENTACAO}, ' \
                    f'{_COLUNA_QUANTIDADE}, {_COLUNA_OBSERVACAO} (%s, %s, %s, %s, %s);'

    _SELECTALL_ = f'select * from {_TABELA_};'
