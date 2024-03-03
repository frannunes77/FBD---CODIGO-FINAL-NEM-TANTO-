class SQLEndereco:
    _TABLE_NAME = 'endereco'
    _COL_ID = 'id'
    _COL_RUA = 'rua'
    _COL_BAIRRO = 'bairro'
    _COL_NUMERO = 'numero'
    _COL_CIDADE = 'cidade'
    _COL_CEP = 'cep'
    _CAMPOS_OBRIGATORIOS = [_COL_RUA, _COL_BAIRRO, _COL_NUMERO, _COL_CIDADE, _COL_CEP]

    _CREATE_TABLE = f'create table if not exists {_TABLE_NAME}'\
                    f'(id serial primary key, ' \
                    f'{_COL_RUA} varchar(50), ' \
                    f'{_COL_BAIRRO} varchar(50), ' \
                    f'{_COL_NUMERO} varchar(50), ' \
                    f'{_COL_CIDADE} varchar(50), ' \
                    f'{_COL_CEP} varchar(50));'

    _INSERT_INTO = f'insert into {_TABLE_NAME}({_COL_RUA}, {_COL_BAIRRO}, {_COL_NUMERO}, {_COL_CIDADE}, {_COL_CEP}) values(%s, %s, %s, %s, %s)'
    _SELECT_BY_RUA = f'select * from {_TABLE_NAME} where {_COL_RUA} ilike %s;'
    _SELECT_ID = f'select * from {_TABLE_NAME} where {_COL_ID}=%s;'
    _SELECT_ALL = f'select * from {_TABLE_NAME};'
    _SELECT_BY_DADOS = f'select count (*) from {_TABLE_NAME} where {_COL_RUA}=%s and {_COL_BAIRRO}=%s and {_COL_NUMERO}=%s' \
                        f' and {_COL_CIDADE}=%s and {_COL_CEP}=%s'

    _SELECT_ID_BY_ENDERECO = f'select {_COL_ID} from {_TABLE_NAME} where {_COL_RUA}=%s and {_COL_BAIRRO}=%s and {_COL_NUMERO}=%s' \
                       f' and {_COL_CIDADE}=%s and {_COL_CEP}=%s'

    _UPDATE_BY_RUA = f'update {_TABLE_NAME} set {_COL_RUA}=%s where {_COL_ID}=%s;'
    _UPDATE_BY_BAIRRO = f'update {_TABLE_NAME} set {_COL_RUA}=%s where {_COL_ID}=%s;'
    _UPDATE_BY_NUMERO = f'update {_TABLE_NAME} set {_COL_NUMERO}=%s where {_COL_ID}=%s;'
    _UPDATE_BY_CIDADE = f'update {_TABLE_NAME} set {_COL_CIDADE}=%s where {_COL_ID}=%s;'
    _UPDATE_BY_CEP = f'update {_TABLE_NAME} set {_COL_CEP}=%s where {_COL_ID}=%s;'

    _DELETE_BY_ENDERECO = f'delete from {_TABLE_NAME} where {_COL_ID}=%s;'