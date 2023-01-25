import peewee

db = peewee.PostgresqlDatabase(
    'orm_py25',
    user='bekjan',
    password='1',
    host='localhost',
    port=5432
)
