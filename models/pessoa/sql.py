from models.endereco.sql import SQLEndereco
class SQLPessoa:
    _TABLE_NAME = 'Pessoa'
    _COL_ID = 'id'
    _COL_TIPO = 'tipo'
    _COL_DOCUMENTO = 'documento'
    _COL_NOME = 'nome'
    _COL_ENDERECO_ID = 'endereco_id'
    _REFERENCES_ENDERECO = f'{SQLEndereco._TABLE_NAME}({SQLEndereco._COL_ID})'

    _CAMPOS_OBRIGATORIOS = [_COL_TIPO, _COL_DOCUMENTO, _COL_NOME, _COL_ENDERECO_ID]

    _CREATE_TABLE = f'create table if not exists {_TABLE_NAME}' \
                    f'(id serial primary key, '\
                    f'{_COL_TIPO} varchar(50), '\
                    f'{_COL_DOCUMENTO} varchar(50),' \
                    f'{_COL_NOME} varchar(50),' \
                    f'{_COL_ENDERECO_ID} integer references {_REFERENCES_ENDERECO});'

    _INSERT_INTO = f'insert into {_TABLE_NAME}({_COL_TIPO}, {_COL_DOCUMENTO}, {_COL_NOME}, '\
                    f'{_COL_ENDERECO_ID}) values(%s, %s, %s, %s);'

    _SELECET_ALL = f'select * from {_TABLE_NAME};'

    _SELECT_ENDERECO_BY_ID = f'select {SQLEndereco._TABLE_NAME}.* from {_TABLE_NAME} join ' \
                              f'{SQLEndereco._TABLE_NAME} on {_TABLE_NAME}.{_COL_ENDERECO_ID} = ' \
                               f'{SQLEndereco._TABLE_NAME}.{SQLEndereco._COL_ID} where {_TABLE_NAME}.{_COL_ID}=%s;'

    _SELECT_ENDERECO_BY_NOME = f'select {SQLEndereco._TABLE_NAME}.* from {_TABLE_NAME} join ' \
                               f'{SQLEndereco._TABLE_NAME} on {_TABLE_NAME}.{_COL_ENDERECO_ID} = ' \
                               f'{SQLEndereco._TABLE_NAME}.{SQLEndereco._COL_ID} where {_TABLE_NAME}.{_COL_NOME}=%s;'

    _SELECT_ID_BY_NOME_TIPO = f'select {_COL_ID} from {_TABLE_NAME} where {_COL_TIPO}=%s and {_COL_DOCUMENTO}=%s and ' \
                               f'{_COL_NOME}=%s;'