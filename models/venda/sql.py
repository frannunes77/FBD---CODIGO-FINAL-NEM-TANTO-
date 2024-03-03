from models.movimentacao.sql import SQLMovimentacao
from models.pessoa.sql import SQLPessoa


class SQLVenda:
    _TABELA = 'Venda'
    _COLUNA_ID = 'id'
    _COLUNA_CLIENTE_ID = 'cliente_id'
    _COLUNA_MOVIMENTACAO_ID = 'movimentacao_id'
    _COLUNA_NUM_NF = 'num_nf'
    _REFERENCES_CLIENTE = f'{SQLPessoa}({SQLPessoa._COL_ID})'
    _REFERENCES_MOVIMENTACAO = f'{SQLMovimentacao}({SQLMovimentacao._COLUNA_ID})'


    _CREATE_TABLE = f'create table if not exists {_TABELA}' \
                    f'({_COLUNA_ID} serial primary key, '\
                    f'{_COLUNA_CLIENTE_ID} integer references {_REFERENCES_CLIENTE}, '\
                    f'{_COLUNA_MOVIMENTACAO_ID} integer references {_REFERENCES_MOVIMENTACAO}, ' \
                    f'{_COLUNA_NUM_NF} varchar(50);'

    _INSERT_INTO = f'inset into {_TABELA}({_COLUNA_CLIENTE_ID}, {_COLUNA_MOVIMENTACAO_ID}, {_COLUNA_NUM_NF} values(%s, %s, %s);'

    _SELECET_ALL = f'select * from {_TABELA};'

