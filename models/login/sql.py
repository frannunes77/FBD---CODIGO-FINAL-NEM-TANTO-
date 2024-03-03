class SQLLogin:
    _TABLE_NAME = 'login'
    _COL_ID = 'id'
    _COL_LOGIN = 'login'
    _COL_SENHA = 'senha'
    _CAMPOS_OBRIGATORIOS = [_COL_LOGIN, _COL_SENHA]

    _CREATE_TABLE = f'create table if not exists {_TABLE_NAME}' \
                    f'({_COL_ID} serial primary key, ' \
                    f'{_COL_LOGIN} varchar(20),' \
                    f'{_COL_SENHA} varchar(20));'

    _INSERT_INTO = f'insert into {_TABLE_NAME}({_COL_LOGIN}, {_COL_SENHA}) values(%s, %s);'
    _SELECT_BY_ID = f'select * from {_TABLE_NAME} where {_COL_ID} = %s;'
    _SELECT_BY_LOGIN = f'select * from {_TABLE_NAME} where {_COL_LOGIN} ilike (%s) limit 1;'
    _SELECT_BY_ALL = f'select * from {_TABLE_NAME};'
    _UPDATE_BY_LOGIN = f'update {_TABLE_NAME} set {_COL_LOGIN}=%s where {_COL_ID}=%s'
    _UPDATE_BY_SENHA = f'update {_TABLE_NAME} set {_COL_SENHA}=%s where {_COL_ID}=%s'
    _DELETE_BY_LOGIN = f'delete from {_TABLE_NAME} where {_COL_ID}=%s'
