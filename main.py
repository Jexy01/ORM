'''
ORM (Object Relation Mapping - обьектно реляционное отображение) - технология которая связывает БД с концепциями обьектно ориентированных языков программтрования. ORM - прослойка между БД и кодом который пишет програмист, которая позволяет создовать в программе обьекты обновлять, удалять и получать их.
'''

#python:
    # peewee
    # sqlalchemy
    # DjangoORM

# Класс - Таблица в БД 
# Атрибут класса - поле в БД
# Обьект класса - строка в таблице

from views import *
from settings import db

db.connect()

get_categories()
get_products()

db.close()